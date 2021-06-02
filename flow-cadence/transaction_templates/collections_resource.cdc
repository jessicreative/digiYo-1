// collections_resource.cdc a.k.a HelloWorldResource.cdc a.k.a ANOTHER account 0x02
//
// This is a variation of the HelloWorld contract that introduces the concept of
// resources, a new form of linear type that is unique to Cadence. Resources can be
// used to create a secure model of digital ownership.
//
// Learn more about resources in this tutorial: https://docs.onflow.org/docs/hello-world

pub contract userCollections {

    // Declare a resource that only includes one function.
    pub resource userAsset { // first time we are seeing userAsset's 

      // **** WORK ON THIS **** 
      //
      // An **** AUCTIONHOUSE **** transaction can call this function to get the "Hello, World!"
      // message from the resource. --> not the "hello, world!" message, 
      // but the NFTs that the user is storing in their collections!
      // (after transactions transpire and are saved into collections using 
      // digiYo_account_transactions.cdc)
      //
      // **** (HelloWorld, a.k.a. digiYo_account_transactions.cdc) ****
      //
      // Going to need to have the categories of these userAssets specified by Fabio and Alex. 
      //
      // **** WORK ON THIS **** 


      pub fun user_collections(): String {
        return "Fabio's list of categories for the NFT's --> call the NFT data here."
      }
    }
  
    init() {
      // Use the create built-in function to create a new instance
      // of the userAsset resource
      let new_user_collections <- create userAsset()
  
      // We can do anything in the init function, including accessing
      // the storage of the account that this contract is deployed to.
      //
      // Here we are storing the newly created userAsset resource
      // in the private account storage
      // by specifying a custom path to the resource
      self.account.save(<-new_user_collections, to: /storage/User_collections)
  
      log("userAsset created and stored")
    }
  }
