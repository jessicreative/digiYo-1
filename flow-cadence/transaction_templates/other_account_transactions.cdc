access(all) contract Transactions {

  // Declare a public field of type String.
  //
  // All fields must be initialized in the init() function.
  access(all) let greeting: String

  // The init() function is required if the contract contains any fields.
  init() {
      self.greeting = "Purchase from account 2."
  }

  // Public function that returns our friendly greeting!
  access(all) fun purchase(): String {
      return self.greeting
  }
}
