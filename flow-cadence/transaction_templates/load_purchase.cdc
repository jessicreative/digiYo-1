// Transaction2.cdc

import Transactions from Batstoi_account.cdc


// This transaction calls the "purchase" method on the userAsset object
// that is stored in the account's storage by removing that object
// from storage, calling the method, and then putting it back in storage

transaction {

    prepare(acct: AuthAccount) {

        // load the resource from storage, specifying the type to load it as
        // and the path where it is stored
        let purchaseResource <- acct.load<@Transactions.userAsset>(from: /storage/Purchase)

        // We use optional chaining (?) because the value in storage
        // may or may not exist, and thus is considered optional.
        log(purchaseResource?.purchase())

        // Put the resource back in storage at the same spot
        // We use the force-unwrap operator `!` to get the value
        // out of the optional. It aborts if the optional is nil
        acct.save(<-purchaseResource!, to: /storage/Purchase)
    }
}