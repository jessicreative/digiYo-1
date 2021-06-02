# Getting set up
In our development process, we used flow testnet to test our smart contracts. 
[Here](https://docs.onflow.org/dapp-deployment/testnet-deployment) is a tutorial created by Flow that leads you through testnet. 

Here's our version of the tutorial for deploying contracts in testnet: 

## 1. Create A Flow Testnet Account

You'll need to have installed the Flow CLI, which can be done easily by following these [steps](https://docs.onflow.org/flow-cli/install)

- ### Generate a key pair (public and private keys):
In a terminal shell (or command line) run:
    flow keys generate
You will be gerneated a Private Key and a Public Key. Store these keys (especially the private key) somewhere safe

- ### Request your account
 Go to [Testnet Faucet](https://testnet-faucet-v2.onflow.org/), enter your public key, and click create new account

- ### Funding your account
 Enter your account address gerneated from before into the Fund Account box.
 
 ## 2. Accessing Flow Testnet
 
 Download the flow.json file in this repository. 
 
 In the "accounts" section, add your testnet account.
 
 In the "keys" section under "my-testnet-account", add your private key information.
 
 
## 3. Deploying Contracts
 Change the names of the contracts in your "deployments" section to the contract you wish to deploy.
 
 Run the deploy command. Make sure you are on the same level as your flow.json file.
     flow project deploy --network=testnet
