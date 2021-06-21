# digiYo

<p align="center">
  <a href = https://batstoi.com/>
    <img width="400" src="BT_logo_color.png" /> 
  </a>
  <a href = https://batstoi.com/xp/>
    <img width="400" src="digiYo_logo.png" /> 
  </a>
</p>
<p align = "center" >
  <b>Welcome to Batstoi's digiYo repository!</b>
  </p>
  
## What is digiYo?

digiYo is [Batstoi’s](https://batstoi.com/) nonfungible token game developed with flow cadence featuring various martial arts through 3D animations created using motion capture technology. 

Our video game provides an interactive and engaging experience for you to make the most out of digiYo. We support in-game buying of card packs, inter-user trading, and more through the [Blocto](https://blocto.portto.io/en/) app.

## What is this repository?
This github repository was made to record our work on a public interface to both receive and offer feedback from the rest of the [flow](https://www.onflow.org/) community! This dev doc includes Cadence files for our digiYo minting based on blockchain and transactions and Node JS files for our webapp. 

## Requirements for following through 
If you wish to run this repository, you will need to [install Flow Command Line (FCL)](https://docs.onflow.org/flow-cli/install). 

## Webapp Design

Creating a webapp utilizing blockchain from scratch may be daunting and confusing. This outline (with a bunch of cool dropdowns) may help you understand the format better!

### Legend
<ul>
  <li> Files that end with "tx" are transactions that involve the movement of items and information associated with the address</li>
  <li> Files that include ".script" are checking information associated with that address
</ul>

<!DOCTYPE html>
<!DOCTYPE html>
<details>
    <summary>app</summary>
    <ul style="list-style-type:none;">
        <li><details>
            <summary><b>api</b></summary>
            RESTful API built with express that sends transactions to Flow using the FLow JS SDK
        </details></li>
        <li><details>
        <summary><b>cadence</b></summary>
          This is where we put the contracts, scripts, and transactions
          where we put the contracts, scripts, transactions
            <ul style="list-style-type:none;">
                <li><details>
                    <summary><b>contracts</b></summary>
                    The root folder that gets dealt by the web server in the end; contains a significant file, index.html
                    <ul style="list-style-type:none;">
                        <li><details>
                            <summary>FungibleToken.cdc</summary>
                                A contract interface that must be conformed by all fungible token contracts. Has the Vault resource, and the Provider, Receiver, and Balance resource interfaces.
                                <ul style="list-style-type:none;">
                                    <li>Has variables: totalSupply (of tokens), TokensInitialzied, TokenWithdrawn, TokensDeposited (emitted events)</li>
                                    <li><details>
                                        <summary>Provider interface</summary>
                                        Has withdraw function (withdrawal amount must be the same as the withdrawn Vault)
                                    </details></li>
                                    <li><details>
                                        <summary>Receiver interface</summary>
                                        Deposit function (takes a Vault)
                                    </details></li>
                                    <li><details>
                                        <summary>Balance interface</summary>
                                        Total balance of a vault (checks if balance is initialized)
                                    </details></li>
                                    <li><details>
                                        <summary>Vault resource (Provider, Receiver, Balance)</summary>
                                        Contains functions to send and receive tokens
                                            <ul style="list-style-type:none;">
                                                <li>balance (variable)</li>
                                                <li>init (balance): initializer with initial balance of vault</li>
                                                <li>withdraw function: check there's enough balance in Vault and updates new balance</li>
                                                <li>deposit function: updates balance</li>
                                            </ul>
                                    </details></li>
                                    <li><details>
                                        <summary>createEmptyVault function</summary>
                                        Creates a Vault with zero balance
                                </ul>
                        </details></li>
                    </ul>
                </details></li>
                <li><details>
                    <summary>Kibble.cdc</summary>
                    Building on the interface of FungibleToken.cdc with admin resources and more specific functions and implementations
                    <ul style="list-style-type:none;">
                        <li>emits: TokensWithdrawn, TokensDeposited, TokensMinted, TokensBurned (when destroyed), MinterCreated</li>
                        <li>Name paths: Storage (Vault and Admin), public (receiver and balance)</li>
                        <li>Total supply of Kibbles in existence</li>
                        <li><details>
                            <summary>Vault resource (following interface)</summary>
                                <ul style="list-style-type:none;">
                                    <li>total balance of vault</li>
                                    <li>initialized balance function</li>
                                    <li>withdraw function and adjustment in balance of original vault and emits event; returns a newly created Vault with that much amount withdrawn</li>
                                    <li>deposit function: adds to the balance from the Vault, emits event, sets the given Vault's balance as 0, and destroys the Vault </li>
                                    <li>destroy function: kibble total supply diminishes by the amount in the balance; if there is more than 0 in self balance, then emits event</li>
                                </ul>
                        </details></li>
                        <li>createEmptyVault: function that returns Vault with balance 0</li>
                        <li><details>
                            <summary>Administrator reesource</summary>
                            createNewMinter that returns a new Minter resource (with the allowed amount)
                        </details></li>
                        <li><details>
                            <summary>Minter resource</summary>
                                <ul style="list-style-type:none;">
                                    <li>allowedAmount: variable for the limit for amount of tokens the minter is allowed to mint</li>
                                    <li><details>
                                        <summary>mintTokens:</summary>
                                            <ul style = "list-style-type: none;">
                                                <li>a function that adds the amount to the Kibble.totalSupply.</li>
                                                <li>subtracts amount from self.allowedAmount count (total allowed)</li>
                                                <li>Returns a newly created Vault with that amount in balance</li>
                                            </ul>
                                    </details> </li>
                                <li>init function: where you set the variable self.allowedAmount to that given in the parameters</li>
                                </ul>
                        </details></li>
                        <li><details>
                            <summary>init function</summary>
                                <ul style="list-style-type:none;">
                                    <li>sets the path variables in actual paths</li>
                                    <li>initializes contract's totalSupply as 0</li>
                                    <li>Creates on true Admin object and deposits it into the contract account</li>
                                    <li>emits tokens initialized event (with totalSupply)</li>
                                </ul>
                        </details></li>
                    </ul>
                </details></li>
                <li><details>
                    <summary>KittyItems.cdc</summary>
                    Building on the NonFungibleToken interface
                        <ul style="list-style-type:none;">
                            <li>has a list of events, paths, and totalSupply of the items minted</li>
                            <li><details>
                                <summary>NFT Resource</summary>
                                    <ul>
                                        <li>Token's ID</li>
                                        <li>Token's type</li>
                                        <li>Init function (for ID and type)</li>
                                    </ul>
                            </details></li>
                            <li><details>
                                <summary>KittyItemsCollectionPublic</summary>
                                Interface that users can cast their KittyItems Collection as to allow others to deposit KittyItems into their Collection. Also allows for reading the details of KittyItems in the Collection
                                    <ul>
                                        <li>deposit function</li>
                                        <li>getIDs function</li>
                                        <li>borrowNFT function</li>
                                        <li>borrowKittyItem function</li>
                                    </ul>
                            </details></li>
                            <li><details>
                                <summary>Collection resource</summary>
                                a collection of kittyItem NFTs owned by an account
                                    <ul style = "list-style-type: none;">
                                        <li>ownedNFTs variable</li>
                                        <li>withdraw function: removes token with key from ownedNFTs, emits event, and returns the token withdrawn</li>
                                        <li><details>
                                            <summary>deposit function</summary>
                                            variable token to take in the NonFungibleToken.NFT token in parameter in as a KittyItems.NFT
                                                <ul style = "list-style-type: none;">
                                                    <li>Sets variable ID</li>
                                                    <li>Adds the new token to the dictionary which removes the old one</li>
                                                    <li>Emits deposit event</li>
                                                    <li>Destroys oldToken</li>
                                                </ul>
                                        </details> </li>
                                        <li>getIds: function that returns an array of the IDs that are in the collection</li>
                                        <li>borrowNFT function: gets a reference to a NFT in the collection so that the caller can read its metadata and call its methods</li>
                                        <li>borrowKittyItme function: gets a reference to a NFT in the collection as a KittyItem, exposing all of its fields (including the typeID); safe as there are no functoins that can be called on the KittyItem</li>
                                        <li>destructor method: destroys the entire list of ownedNFTs</li>
                                        <li>initializer to create empty list for ownedNFTs</li>
                                    </ul>
                            </details></li>
                            <li>createEmptyCollection function: anyone can call this function to create a new empty collection</li>
                            <li><details>
                                <summary>NFTMinter Resource</summary>
                                Resource that an admin or similar would be able to mint new NFTs.
                                    <ul style = "list-style-type: none;">
                                        <li><details>
                                            <summary>mintNFT function</summary>
                                        
                                                <ul style = "list-style-type: none;">
                                                    <li>Mints a new NFT with a new ID and deposit it in the recipients collection using their collection reference.</li>
                                                    <li>currently sets their id as KittyItems.totalSupply and update supply to +1 at the end</li>
                                                </ul>
                                        </details></li>
                                    </ul>
                            </details></li>
                            <li><details>
                                <summary>fetch function</summary>
                                    <ul style = "list-style-type: none;">
                                        <li>Gets a reference to a KittyItem from an account's Collection, if available</li>
                                        <li>If an account does not have a KittyItmes.Collection, panic</li>
                                        <li>If an account has a collection but does not contaiin the itemID, return nil</li>
                                        <li>If an account has a collection and that collection contains the itemID, return a reference to that</li>
                                    </ul>
                            </details></li>
                            <li><details>
                                <summary>init function</summary>
                                    <ul style = "list-style-type: none;">
                                        <li>Sets the name paths</li>
                                        <li>Initializes totalSupply to 0</li>
                                        <li>Creates a minter resource and saves it to storage</li>
                                        <li>Emits event.</li>
                                    </ul>
                            </details></li>
                        </ul> 
                </details></li>
                <li><details>
                    <summary>KittyItemsMarket.cdc</summary>
                    A simple KittyItems initial sale contract for the DApp to use in order to list and sell KittyItems
                        <ul style = "list-style-type: none;"></ul>
                            <li><details>
                                <summary>SUMMARY</summary>
                                Its structure is neither what would be if it was the simplest possible market contract or if it was a complete general purpose market contract. Rather, it iis the simplest possible version of a more general purpose market contract that indicates how that contract might function in broad strokes. This has been done so that integrating with this contract is a useful preparatory exercise for code that will integrate with the later more general purpose market contract.
                                    <ul style = "list-style-type: none;"></ul>
                                        <li><details>
                                            <summary>It allows: </summary>
                                                <ul style = "list-style-type: none;">
                                                    <li>Anyone to create Sale Offers and place them in a collection, making it publically accessible</li>
                                                    <li>Anyone to accept the offer and buy the item.</li>
                                                </ul>
                                        </details></li>
                                        <li><details>
                                            <summary>It notably does not handle: </summary>
                                                <ul style = "list-style-type: none;"></ul>
                                                    <li>Multiple different sale NFT contracts</li>
                                                    <li>Multple different payment FT contracts</li>
                                                    <li>Splitting sale payments to multiple recipients</li>
                                        </details></li>
                            </details></li>
                            <li>sale offer events (created, accepted, finished) and collection events (removed/inserted from/to collection)</li>
                            <li>name paths</li>
                            <li>interface providing read-only view of a saleOffer</li>
                            <li><details>
                                <summary>SaleOffer resource</summary>
                                A KittyItems NFT being offered to sale for a set fee paid in Kibble.
                                    <ul style = "list-style-type: none;">
                                        <li><details>
                                            <summary>Variables</summary>
                                            saleCompleted, itemID, price, collection containing that ID (sellerItemProvider), the Kibble Vault that will receive that payment if the sale complete successfully (sellerPaymentReceiver)
                                        </details></li>
                                        <li><details>
                                            <summary>accept function</summary>
                                            Called by a purchaser to accept the sale offer; if they send the correct payment in Kibble and if the item is still available, the KittyItems NFT will be place in their KittyItems.Collection
                                        </details></li>
                                        <li><details>
                                            <summary>destroy function </summary>
                                            whether the sale if finished or not, emit withdrawn event
                                        </details></li>
                                        <li><details>
                                            <summary>init function</summary>
                                            Takes the information required to create a sale offer, notably the capability to transfer the KittyItems NFT and the capability to receive Kibble in payment
                                        </details></li>
                                        <li><details>
                                            <summary>createSaleOffer function</summary>
                                            Make creating a SaleOffer publicly accessible; Returns SalesOffer with required metadata</details></li>
                                                <li><details>
                                                    <summary>CollectionManager resource</summary>
                                                    <ul style = "list-style-type: none;">
                                                        <li>An interface for adding and removing SaleOffers to a collection, intended for use by the collection's owner</li>
                                                        <li>Has Insert and Remove functions</li>
                                                    </ul>
                                            </details></li>
                            
                                        <li><details>
                                            <summary>CollectionPurchaser resource</summary>
                                                <ul style = "list-style-type: none;">
                                                    <li>An interface for allowing purchasing items via SaleOffers in a collection</li>
                                                    <li>Also provided by CollectionPublic; it is here to support more fine-grained access to the collection for yet unspecified future use cases</li>
                                                    <li>Contains purchase function with itemID, buyerCollection, and buyerPayment Vault</li>
                                                </ul>
                                        </details></li>
                                        <li><details>
                                            <summary>CollectionPublic interface</summary>
                                            An interface to allow listing and borrowing SaleOffers, and purchasing items via SaleeOffers in a collection</li>
                                                <ul style = "list-style-type: none;">
                                                    <li>Functions: getSaleOfferIDs, borrowSaleItem, purchase</li>
                                                </ul>
                                        </details></li>

                                        <li><details>
                                            <summary>Collection resource</summary>
                                            A resource that allows its owner to manage a list of SaleOffers, and purchasers to interact with them
                                                <ul style = "list-style-type: none;">
                                                    <li>variable: saleOffers</li>
                                                    <li><details>
                                                        <summary>insert saleOffer function (with itemID, typeID, price)</summary>
                                                        add the new offer to the dictionary which removes the old one and emit event with required metadata
                                                    </details></li>
                                                    <li><details>
                                                        <summary>remove function</summary>
                                                        Remove and return a SaleOffer from the collection and emit event.
                                                    </details></li>
                                                    <li><details>
                                                        <summary>purchase function</summary>
                                                        If the caller passes a valid itemID for an item that is still for sale and passes a Kibble Vault typed as FungibleToken.Vault (Kibble.deposit() handles the type safety of this) containing the correct payment amount, this will transfer the KittyItem to the caller's KittyItems collection. It will then remove and destroy the offer. Note that this menas that events will be emitted in this order:
                                                            <ol>
                                                                <li>Collection.CollectionRemovedSaleOffer</li>
                                                                <li>KittyItems.Withdraw</li>
                                                                <li>KittyItems.Deposit</li>
                                                                <li>SaleOffer.SaleOfferFinished</li>
                                                            </ol>
                                                    </details></li>
                                                    <li><details>
                                                        <summary>getSaleOfferIds function</summary>
                                                        Returns an array of the IDs that are in the collection.
                                                    </details></li>
                                                    <li><details>
                                                        <summary>borrowSaleItem</summary>
                                                            <ul style = "list-style-type: none;">
                                                                <li>Returns an optional read-only view of the SaleItem for the given itemID if it is contained by this collection</li>
                                                                <li>The optional view will be nil if the provded itemID is not present in the collection</li>
                                                            </ul>
                                                    </details></li>
                                                    <li>destroy saleOffers function</li>
                                                    <li>init saleOffers as empty list function</li>
                                                </ul>
                                        </details></li>
                                        <li>createEmptyCollection function: make creating a Collection publicly accessible</li>
                                        <li>init: set actual paths</li>
                                    </ul>
                            </details>
                </details></li>
        <!-- </details></li> -->
                <li><details>
                    <summary>NonFungibleToken.cdc</summary>
                    The interface that all non-fungible token contracts could conform to. 
                    If a user wants to deploy a new nft contract, their contract would need to implement the NonFungibleToken interface.
                        <ul style="list-style-type:none;">
                            <li><details>
                                <summary>NonFungibleToken interface</summary>
                                    <ul style="list-style-type:none;">
                                        <li>totalSupply</li>
                                        <li>event emitted (ContractInitialized, Withdraw, Deposit)</li>
                                        <li>interface INFT (unique id): Interface that NFTs have to conform to </li>
                                        <li>resource NFT (conforming to INFT): Requirment that all conforming NFT smart contracts have to define a resource called NFT that conforms to INFT</li>
                                        <li><details>
                                            <summary>Provider resource interface</summary>
                                                <ul style="list-style-type:none;">
                                                    <li>withdraw function: withdraw removes an NFT from the colletion and moves it to the caller</li>
                                                </ul>
                                        </details></li>
                                        <li><details>
                                            <summary>Receiver resource interface</summary>
                                            Interface to mediate deposits to the Collection
                                                <ul style="list-style-type:none;">
                                                    <li>deposit function: deposit takes an NFT as an argument and adds it to the Collection</li>
                                                </ul>
                                        </details></li>
                                        <li><details>
                                            <summary>CollectionPublic resource interface</summary>
                                            Interface that an account would commonly publish for their collection
                                                <ul>
                                                    <li>deposit</li>
                                                    <li>getIDs</li>
                                                    <li>borrowNFT</li>
                                                </ul>
                                        </details></li>
                                        <li><details>
                                            <summary>Collection resource</summary>
                                                <ul style="list-style-type:none;">
                                                    <li>conforms to Provider, Receiver, and CollectionPublic interfaces</li>
                                                    <li>Requirement for the concrete resource type to be declared in the implementing contract</li>
                                                    <li><details>
                                                        <summary>Contains:</summary>
                                                        ownedNfts dictionary, withdrawal function, deposit function, getIDs (returned as an array) function, borrowNFT function
                                                    </details></li>
                                                </ul>
                                        </details></li>
                                        <li>createEmptyCollection (according to Collection interfact) function</li>
                                    </ul>
                            </details></li>
                        </ul>
                </details></li>
                </ul>
                </details>
            </li>
            <li><details>
                <summary><b>lib</b></summary>
                Tests with JS Testing Framework and Go Testing
            </details></li>
            <li><details>
                <summary><b>scripts</b></summary>
                <ul style="list-style-type:none;">
                <li><details>
                  <summary><b>kibble</b></summary>
                  <ul style="list-style-type:none;">
                    <li><details>
                        <summary>get_balance.cdc</summary>
                        This script returns an account's Kibble balance.
                    </details></li>
                    <li><details>
                        <summary>get_supply.cdc</summary>
                        This script returns the total amount of Kibble currently in existence.
                        </details></li>
                    </ul>
                </details></li>  
                <li><details>
                    <summary><b>kittyItems</b></summary>
                        <ul style="list-style-type:none;">
                        <li><details>
                            <summary>get_collection_ids.cdc</summary>
                          This script returns an array of all the NFT IDs in an account's collection.
                        </details></li>
                        <li><details>
                            <summary>get_collection_length.cdc</summary>
                            This script returns the size of an account's KittyItems collection.
                            </details></li>
                        <li><details>
                            <summary>get_kitty_item_type_id.cdc</summary>
                            This script returns the metadata for an NFT in an account's collection.
                        </details></li>
                        <li><details>
                            <summary>get_kitty_items_supply.cdc</summary>
                            This script returns the number of KittyItems currently in existence.
                            </details></li>
                        </ul>
                  </details></li>  
                <li><details>
                    <summary><b>kittyItemsMarket</b></summary>
                    <ul style="list-style-type:none;">
                    <li><details>
                        <summary>get_collection_ids.cdc</summary>
                        This script returns an array of all the NFT IDs for sale in an account's SaleOffer collection 
                        </details></li>
                    <li><details>
                        <summary>get_collection_legnth.cdc</summary>
                        This script returns the size of an account's SaleOffer collection
                    </details></li>
                    </ul>
            </ul>
            </details></li>
            <li><details>
                <summary><b>transactions</b></summary>
                <ul style="list-style-type:none;">
                    <li><details>
                        <summary>build-all.sh</summary>
                        Install and run web and api
                    </details></li>
                    <li><details>
                        <summary>run-local.sh</summary>
                        exports a lot of env variables (like flow address, private and public keys, fungible and NFT addresses, API url, etc.) Runs lerna.
                    </details></li>
                    <li><details>
                        <summary>run-testnet.sh</summary>
                        Similar to run-local.sh except it doesn't have private and public keys and is ran on testnet instead of the emulator
                    </details></li>
                    <li><details>
                        <summary>setup-minter.sh</summary>
                        <ul style="list-style-type:none;">
                        <li><details>
                            POST HTML requests to set up minter account (for kibbles, kitty-items, market)
                        </details></li>
                        <li>
                            <details>
                                <summary>POST HTML requests to mint Kibbles and KittyItems</summary>
                                50 default kibbles; typeID1 and itemID 0 and price 7.5 as default
                            </details>
                        </li>
                        </ul>
                        
                    </details></li>
                </ul>
            </details></li>
        </details></li>
        
        <li><details>
        <summary><b>web</b></summary>
            <ul style="list-style-type:none;">
                <li><details>
                    <summary><b>public</b></summary>
                    The root folder that gets dealt by the web server in the end; contains a significant file, index.html
                    <ul style="list-style-type:none;">
                    <li><details>
                        <summary>index.html</summary>
                        THE single html page in our project containing the ID root on line 18, where we place our React application.
                    </details>
                    <li><details>
                        <summary>manifest.json</summary>
                        Gives information to the broswer about your application. For example, this is required for mobile browsers so that you can add a shortcut to your web application.
                        </details>
                    </ul>
                    </details>
                </li>
                <li><details>
                    <summary><b>src</b></summary>
                    <ul style="list-style-type:none;">
                        <li><details>
                            <summary>parts folder</summary>
                            Contains general components that use one or more Hooks and one or more display components.
                        </details>
                        <li><details>
                            <summary><b>svg</b></summary>
                            Contains images of NFTs and logos.
                            <ul style = "list-style-type:none;">
                                <li>
                                    <details>
                                        <summary><b>items</b></summary>
                                        Contains images of NFTs
                                    </details>
                              </li>
                            </ul>
                            </details>
                        <li><details>
                            <summary><b>util</b></summary>
                            Contains small single-purpose funcitons, without dependencies, free of side effects, and format values (to print and view in UI). 
                            <ul style = "list-style-type:none;">
                                <li><details>
                                    <summary>fetcher.js</summary>
                                <ul>
                                    <li>a function that returns the data (formatted in json) from a url</li>
                                    <li>Will be imported and called in use_market_items.hook.js to fetch data in line 22 in funciton useSWR()</li>
                                </ul>
                            </details></li>
                            <li><details>
                                <summary>fmt-flow.js</summary>
                                <ul>
                                    <li>a function for displaying flow balance (as a string)</li>
                                    <li>imported and called in flow-balance-cluster.comp.js to show flow balance in a label on line 16.</li>
                                </ul>
                            </details></li>
                            <li><details>
                                <summary>fmt-kibble.js</summary>
                                <ul>
                                    <li>a function for displaying coin (digiyo currency) balance as a cleaned up string.</li>
                                    <li>imported and called in balance-cluster.comp.js to show coin balance in table data in line 45 and also in kibbles-balance-cluster.comp.js to show coin balance in label in line 18.</li>
                                </ul>
                            </details></li>
                            <li><details>
                                <summary>normalize-item.js</summary>
                                <ul>
                                    <li>a function that (given an item (json data fetched from useSWR) as parameter) returns an object assoicated with metadata, item id, type id, owner, price, and transaction id.</li>
                                    <li>Where it is called: after fetching data using useSWR in use-market-items.hook.js, if successful, it will take a list given by some parent component, loop through all the items fetched previously, make them into objects with metadata, then set the parent's list as a list of objects with those formatted data. See line 29.</li>
                                </ul>
                            </details></li>
                            <li><details>
                                <summary>sleep.js</summary>
                                <ul>
                                    <li>a function to make the code wait (default wait time = 500 miliseconds) before executing the next line of code.</li>
                                    <li>since Javascript is asynchronous, this means you can't pause/block code execution, so you must use this funciton to make things wait </li>
                                    <li>use in use-initialized.hook.js where it returns a function that maintains variables about whether the account is initialized, its status, flow and kibble (coiin) balance. It updates by calling the initializeAccount function (status PROCESSSING). If successful, it refreshes the flow kibble balance and sets SUCCESS status. When initialization and update process is complete, it calls the SLEEP (delay time) to wait and then reset the status back ot IDLE. See line 73.</li>
                                </ul>
                            </details></li>
                            </ul>
                        </details></li>
                        <li>index.js</li>
                        <li><details><summary>font.css and theme.js</summary>
                        Files for installed UI theme and font</details></li>
                    </ul>
                </details></li>
                <li>
                    <details>
                        <summary>.env.example</summary>
                        Contains environment variables.
                    </details>
                </li>
                <li>
                    <details>
                        <summary>package.json and package-lock.json</summary>
                        Json file to install dependencies; automatically created with <code>create-react-app</code>.
                    </details>
                </li>
            </ul>
        </details></li>
        <li>
            <details>
                <summary>app.json</summary>
                Contains information about the flow account such as the address and private key. 
            </details>
        </li>
        <li>
            <details>
                <summary>flow.json</summary>
                Where you can update/add/delete the names and file locations of the contracts as they are created and specifiy which network the contracts are deployed to.
            </details>
            </li>
            <li>
            <details>
                <summary>.env</summary>
                Stores FLOW_ADDRESS and FLOW_PRIVATE_KEY. 
            </details>
            </li>
            <li>
                <details>
                    <summary>.gitignore</summary>
                    Contains information that you do not want to commit to git, such as the .env file. 
                </details>
                </li>

    </ul>
</details>
