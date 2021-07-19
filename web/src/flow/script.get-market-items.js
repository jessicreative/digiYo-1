import * as fcl from "@onflow/fcl"
import * as t from "@onflow/types"

const CODE = fcl.cdc`
  import digiYoItemsMarket from 0xdigiYoItemsMarket

  pub fun main(address: Address): [UInt64] {
    if let col = getAccount(address).getCapability<&digiYoItemsMarket.Collection{digiYoItemsMarket.CollectionPublic}>(digiYoItemsMarket.CollectionPublicPath).borrow() {
      return col.getSaleOfferIDs()
    } 
    
    return []
  }
`

export function fetch_PrimaryMarketItems(address) {
  if (address == null) return Promise.resolve([])

  // prettier-ignore
  return fcl.send([
    fcl.script(CODE),
    fcl.args([
      fcl.arg(address, t.Address)
    ])
  ]).then(fcl.decode).then(d => d.sort((a, b) => a - b))
}
