// Transaction1.cdc

// **** WORK ON THIS... WHAT IS THIS FOR?? ****
// **** WHAT IS AuthAccount ??? -> ask Jessica ****

import digiyo_NFT from uncommon.cdc // instead of 0x01?

// This transaction checks if an NFT exists in the storage of the given account
// by trying to borrow from it

transaction {
    prepare(acct: AuthAccount) {
        if acct.borrow<&digiyo_NFT.NFT>(from: /storage/NFT1) != nil {
            log("The token exists!")
        } else {
            log("No token found!")
        }
    }
}
}