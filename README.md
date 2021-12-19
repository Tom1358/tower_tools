Tower Tools

Church bell ringing, and campanology, is a hobby that continues to attract people even into the twenty-first century; however, for tower captains (who manage the ringers) and steeple keepers (who maintain the towers) it can have many challenges - recruitment and retaining ringers as a voluntary hobby and training them up is always something that requires assistance in the form of equipment, tools, ideas and resources.  Maintaining a tower involves knowledge of rope, bell and wood/ frame maintenance, and knowing who or where to go for assistance, know-how and specific items for the industry.

This site aims to act as a hub for people interested in tower maintenance or ringing development to purchase items that would be of value, and also to provide merchandise to help boost financial resources that can help the ringing community.

Contents

UX
Structure
Technologies Used
Testing
Deployment
Credits

# UX
## User Stories

<details>
<summary>Viewing & Navigation</summary>

| As a…   | I want to be able to…                               | …so that I can…                                                  |
|---------|-----------------------------------------------------|------------------------------------------------------------------|
| shopper | view a list of all products                         | See what the website has to offer as a whole                     |
|         | View a list of specific/ categorised products       | Filter through products to view/ purchase what is relevant to me |
|         | View individual product details                     | Look at specific item details to ensure it is the thing I want   |
|         | View the total cost of my basket/ planned purchases | Ensure I stick to budget/ do not spend too much on the site      |
</details>

---
<details>
<summary>Registration & Sign-in</summary>

| As a…     | I want to be able to…            | …so that I can…                                                                              |
|-----------|----------------------------------|----------------------------------------------------------------------------------------------|
| Site user | Easily register for an account   | have an account to view my personalised user profile                                         |
|           | Easily log in/ out               | Access my account information securely and safely, knowing my details are secure             |
|           | Have a personalised user profile | view personal order history, save payment information, and save a basket for future browsing |
</details>

---
<details>
<summary>Sorting & Searching</summary>

| As a…   | I want to be able to…                                       | …so that I can…                                                              |
|---------|-------------------------------------------------------------|------------------------------------------------------------------------------|
| Shopper | Search for products by name or description                  | Find whether a specific product is available on the site to purchase         |
|         | Easily see what I've searched for and the number of results | Get the results for a search at a glance, and see what availability there is |
</details>

---
<details>
<summary>Purchase & Checkout</summary>

| As a…   | I want to be able to…                                       | …so that I can…                                                                         |
|---------|-------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Shopper | Easily select the number of items to add to my basket       | Easily add more items if required (e.g. six new items)                                  |
|         | View items in my basket I plan to purchase                  | have an overview/ summary of what I am buying in total                                  |
|         | Be able to update or delete any items in my shopping basket | Easily prevent buyer's remorse, or splash out on more if required                       |
|         | Safely, securely and easily enter payment information       | Purchase items from the website without worrying about the safety/ security of doing so |
|         | View an order summary before submitting a payment           | Review my purchases before it submits                                                   |
|         | View an order confirmation after submitting a payment       | Confirm that everything went through correctly                                          |
|         | Receive an email confirmation after submitting a payment    | Have a record of what I have paid for, and when                                         |
</details>

---
<details>
<summary>Site Admin</summary>

| As a…      | I want to be able to… | …so that I can…                                              |
|------------|-----------------------|--------------------------------------------------------------|
| Site Admin | Add a product         | Add new items to the online store                            |
|            | Update a product      | Change any details of any products if required               |
|            | Delete a product      | Remove a product from the store if it is no longer available |
</details>

---
<details>
<summary>Product Reviews</summary>

| As a…      | I want to be able to…                                                  | …so that I can…                                                                     |
|------------|------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Shopper    | Leave a review of a product I have bought - in the format of 1-5 stars and a comment | Share my thoughts on the product with other shoppers                                |
| Site admin | Remove a review                                                        | Remove any review if it is deemed offensive/ not relevant/ not acceptable for site. |
</details>

---
# Structure
## Overview of Site and Page Structure

## Wireframes for Skeleton of Website

## Colour theme(s) and Styling

Font chosen:
- For logo - Stencil
- For website text/ headers - Oxygen



# Technologies Used
## Languages

## Libraries & Frameworks

## Editors

## Tools

## Deployment Platform




# Testing




# Deployment

This project has been developed using Gitpod and GitHub.  The website resides as a repository in GitHub, and has been deployed using Heroku.  Static files are stored using Amazon AWS in an Amazon Web Services S3 Bucket.

## to Fork this project

## to Clone this project

## to Download this project

## Necessary Environment Variables (if cloning/ forking project)

| Variable              | Value                             |
|-----------------------|-----------------------------------|
| DEVELOPMENT           | True                              |
| SECRET_KEY            | `your_django_secret_key`          |
| HEROKU_HOSTNAME       | `appname.herokuapp.com`           |
| STRIPE_PUBLIC_KEY     | `your_stripe_public_key`          |
| STRIPE_SECRET_KEY     | `your_stripe_secret_key`          |
| STRIPE_WH_SECRET      | `your_stripe_webhook_secret_key`  |


## to deploy the website to Heroku

1. Sign in to heroku.com, create a new app (*new* button at top right of dashboard), and on the Deploy tab select GitHub as deployment method.
2. Connect to the relevant repository.
3. At heroku.com, go to the Resources tab, and type in Postgres.  Select Heroku Postgres, and Submit.  This will install POSTGRES.
4. In the GitHub CLI, using PIP3, install `psycopg2-binary` and `gunicorn`.  You can confirm the Heroku app has the POSTGRES db by logging in (`heroku login -i`) and the command `heroku addons`.  Then, use PIP3 to install `dj_database_url`.  Create a `requirements.txt` file with the CLI command `pip3 freeze --local > requirements.txt`, to list all the Python dependencies.
5. Confirm at heroku.com in Settings > Config Vars that there is the link for the new db available.
6. In settings.py, in the DATABASES section, remove the original SQLite3 code, include the Heroku POSTGRES database URL `'default': dj_database_url.parse(...)`, and `import dj_database_url` at the top.
7. Also in settings.py, add `ALLOWED_HOSTS = [os.environ.get('HEROKU_HOSTNAME')]`
8. Show, plan and complete migrations (`python3 manage.py showmigrations`, `python3 manage.py migrate --plan`, `python3 manage.py migrate`) to ensure that this new db is linked up and working.  This will then populate it with the necessary data.
9. Create a Procfile with the line `web: gunicorn`[app name]`.wsgi:application`.  Now is a good time to update the `requirements.txt` file and add, commit and push to GitHub.
10. Generate a Django secret key using [miniwebtool.com](www.miniwebtool.com)
11. At heroku.com, in Settings > Config Vars, ensure the following variables and values are set:

| Variable              | Value                    |
|-----------------------|--------------------------|
| DISABLE_COLLECTSTATIC | 1                        |
| SECRET_KEY            | `your_django_secret_key` |
| HEROKU_HOSTNAME       | `appname.herokuapp.com`  |

12. Confirm the app is connected to the correct GitHub repository, and enable Automatic Deploys in the Deploy tab.
13. The above settings mean that now when anything is pushed to GitHub, it will automatically be sent to Heroku, which will build the app with the required packages and dependencies.
14. Comfirm that the application is automatically deploying to Heroku by checking the build log in the activity tab; the app in Heroku is now successfully linked to GitHub.


## to deploy static files to Amazon AWS, and configure Heroku to read static files from Amazon AWS

## to configure Stripe for the deployed site




# Credits
## Design and Research
- Code: Institute's 'Boutique Ado' project - for the use of Django in an e-commerce environment

## Content - Images and Text


## Support


# Disclaimer - this site is not designed for professional use.  It has been developed as a learning project for getting to grips with the Python framework Django, and should be deemed as such.







![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Tom1358,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
