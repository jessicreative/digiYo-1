import Transactions from primary_marketplace_transactions.cdc

transaction {

  prepare(acct: AuthAccount) {}

  execute {
    log(Transactions.purchase())
  }
}