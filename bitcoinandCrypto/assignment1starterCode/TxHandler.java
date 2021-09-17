import java.util.ArrayList;

public class TxHandler {

    private UTXOPool utxoPool;

    /**
     * Creates a public ledger whose current UTXOPool (collection of unspent transaction outputs) is
     * {@code utxoPool}. This should make a copy of utxoPool by using the UTXOPool(UTXOPool uPool)
     * constructor.
     */
    public TxHandler(UTXOPool utxoPool) {
        utxoPool = new UTXOPool(utxoPool);
    }

    /**
     * @return true if:
     * (1) all outputs claimed by {@code tx} are in the current UTXO pool, 
     * (2) the signatures on each input of {@code tx} are valid, 
     * (3) no UTXO is claimed multiple times by {@code tx},
     * (4) all of {@code tx}s output values are non-negative, and
     * (5) the sum of {@code tx}s input values is greater than or equal to the sum of its output
     *     values; and false otherwise.
     */
    public boolean isValidTx(Transaction tx) {
        
        double totalInput = 0;
        double totalOutput = 0;

        ArrayList<UTXO> pastUTXO = new ArrayList<>();

        for (int i=0;i<tx.numInputs();i++) {
            Transaction.Input input = tx.getInput(i);
            int outputIndex = input.outputIndex;
            byte[] prevTxHash = input.prevTxHash;
            byte[] signature = input.signature;

            UTXO utxo = new UTXO(prevTxHash, outputIndex);

        // Rule 1:
            if (!utxoPool.contains(utxo)) {
                return false;
            }
        
        //Rule 2
            Transaction.Output output = utxoPool.getTxOutput(utxo);
            byte[] message = tx.getRawDataToSign(i);
            if (!Crypto.verifySignature(output.address,message,signature)) {
                return false;
            }
        
        //Rule 3
            if (pastUTXO.contains(utxo)) {
                return false;
            }
            pastUTXO.add(utxo);
            totalInput += output.value;
        }
    
        //Rule 4
        for (int i=0;i<tx.numOutputs();i++) {
            Transaction.Output output = tx.getOutput(i);
            if (output.value < 0) {
                return false;
            }
            totalOutput += output.value;
        }

        //Rule 5
        if (totalInput < totalOutput) {
            return false;
        }
        return true;
    }

    /**
     * Handles each epoch by receiving an unordered array of proposed transactions, checking each
     * transaction for correctness, returning a mutually valid array of accepted transactions, and
     * updating the current UTXO pool as appropriate.
     */
    public Transaction[] handleTxs(Transaction[] possibleTxs) {
        ArrayList<Transaction> validTxs = new ArrayList<>();
        for (Transaction t : possibleTxs) {
            if (isValidTx(t)) {
                validTxs.add(t);

                //remove utxo
                for (Transaction.Input input : t.getInputs()) {
                    int outputIndex = input.outputIndex;
                    byte[] prevTxHash = input.prevTxHash;
                    UTXO utxo = new UTXO(prevTxHash, outputIndex);
                    utxoPool.removeUTXO(utxo);
                }
                //add new utxo
                byte[] hash = t.getHash();
                for (int i=0;i<t.numOutputs();i++) {
                    UTXO utxo = new UTXO(hash, i);
                    utxoPool.addUTXO(utxo, t.getOutput(i));
                }
            }
        }
        Transaction[] validTxsArr = new Transaction[validTxs.size()];
        validTxsArr = validTxs.toArray(validTxsArr);
        return validTxsArr;
    }

}
