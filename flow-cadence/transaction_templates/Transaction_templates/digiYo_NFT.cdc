// digiyo_NFT.cdc
//
// The NonFungibleToken contract is a sample implementation of an uncommon card/non-fungible token (NFT) on Flow.
//
// This contract defines one of the simplest forms of NFTs using an
// integer ID and metadata field.
// 
// Learn more about non-fungible tokens in this tutorial: https://docs.onflow.org/docs/non-fungible-tokens

*/
// WHAT WE ARE DOING HERE is setting up our NFT's that exist within the Batstoi_account ecosystem. 
// We have multiple tiers, which will be called in this overarching digiYo_NFT contract and are determined
// by their point value and given a unique user id. What algorithm determines this user id is yet to be 
// determined. 
/*

pub contract digiyo_NFT {

    // Declare the NFT resource type
    pub resource NFT {
        // The unique ID that differentiates each NFT
        pub let id: UInt64

        // String mapping to hold metadata
        pub var metadata: {String: String} //plug in different metadata

        // WHAT WE NEED HERE: 
        // - Tiers of NFT's 
        // - value
        // - clothing randomizer
        // - others...Alex?
        // - ask Jessica, how are we getting the unique ID that differentiates each NFT here? 
        //   what algo are we using?

        // - Ask Jessica, is she differentiating between common and uncommon cards in Smart Contracts or am I? 

        // for x amount of points, call common 
            // metadata: common, file itself,...
            */ IE: 
                execute {
                let metadata : {String : String} = {
                "fan_number": "8",
                "wing_color": "gray", 
                "tips_color": "yellow", 
                "angular_speed": "1.5",
                "uri": "ipfs://QmdTzRu6cP1cWGDZzW93yFCnkCRuSzCju4J3N83TbMVPiM"
                // ID of card itself (rarity of card) //
      }
      /*
            // return NFT id 

        // for y amount of points, call uncommon
            // code for uncommon
            // metadata
            // return NFT id

        // for z amount of points, call rare 
            // code for rare 
            // metadata
            // return NFT id

        // for a amount of points, call legendary 
            // code for legendary 
            // metadata
            // return NFT id 

        // Initialize both fields in the init function
        init(initID: UInt64) {
            self.id = initID
            self.metadata = {}
        }
    }

    // Create a single new NFT and save it to account storage
	init() {
		self.account.save<@NFT>(<-create NFT(initID: 1), to: /storage/NFT1)
	}
}