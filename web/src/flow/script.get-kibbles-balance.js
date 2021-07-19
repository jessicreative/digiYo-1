import {send, decode, script, args, arg, cdc} from "@onflow/fcl"
import {Address} from "@onflow/types"

const CODE = cdc`
  import FungibleToken from 0xFungibleToken
  import digiYo_tokens from 0xdigiYo_tokens

  pub fun main(address: Address): UFix64? {
    if let vault = getAccount(address).getCapability<&{FungibleToken.Balance}>(Kibble.BalancePublicPath).borrow() {
      return vault.balance
    }
    return nil
  }

`

export function fetchdigiYo_tokensBalance(address) {
  if (address == null) return Promise.resolve(false)

  // prettier-ignore
  return send([
    script(CODE),
    args([
      arg(address, Address)
    ])
  ]).then(decode)
}
