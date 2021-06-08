# digiYo

<p align="center">
  <a href = https://batstoi.com/>
    <img width="400" src="BT_logo_color.png" /> 
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

# Webapp Design

Creating a webapp utilizing blockchain from scratch may be daunting and confusing. This legend (with a bunch of cool dropdowns) may help you understand the format better!



<details>
    <summary>app</summary>
    <ul>
        <li>api folder</li>
    </ul>
    <ul style="list-style-type:none;">
        <li><details>
        <summary>cadence folder</summary>
          This is where we put the contracts, scripts, and transactions
          where we put the contracts, scripts, transactions
        </details></li>
        <li><details>
        <summary>web folder</summary>
            <ul style="list-style-type:none;">
                <li><details>
                    <summary><b>public folder</b></summary>
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
                    <summary>src folder</summary>
                    <ul style="list-style-type:none;">
                        <li><details>
                            <summary>parts folder</summary>
                            Contains general components that use one or more Hooks and one or more display components.
                        </details>
                        <li><details>
                            <summary>svg folder</summary>
                            Contains images of NFTs and logos.
                            <ul style = "list-style-type:none;">
                                <li>
                                    <details>
                                        <summary>items folder</summary>
                                        Contains images of NFTs
                                    </details>
                                </li>
                                
                            </ul>
                            </details>
                        <li><details>
                            <summary>util folder</summary>
                            Contains small single-purpose funcitons, without dependencies, free of side effects, and format values (to print and view in UI). 
                            <ul style = "list-style-type:none;">
                                <details>
                                    <summary>fetcher.js</summary>
                                
                                <ul>
                                    <li>a function that returns the data (formatted in json) from a url</li>
                                    <li>Will be imported and called in use_market_items.hook.js to fetch data in line 22 in funciton useSWR()</li>
                                </ul>
                            </details>
                            </ul>
                        </details></li>
                    </ul>
                </details></li>
            </ul>
            
        </details>
    </ul>
</details>
