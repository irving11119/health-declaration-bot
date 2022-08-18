# NUS Health Declaration Bot

## Getting Started

To get started, clone the respository within a terminal and move into the directory of the repository.

```
git clone https://github.com/irving11119/health-declaration-bot.git
cd health-declaration-bot
```

## Required Packages

To install required packages, run the following command below.

```bash
pip install -r requirements.txt
```

## Submitting Temperature Once

Create a .env file in the same directory as health_declaration.py. Within the .env file, enter your NUS username credentials, password and the VAF Client ID of the page in question.

To run the script once for sole temperature update, simply run the following command in terminal in the correseponding directory (For Linux/MacOS)

```bash
python3 health_declaration.py
```

## Automating the Process

Aternatively, we can handle automate our script to submit the temperature twice a day at the appropriate time periods. On Linux systems or Mac, we achieve this by using Cron and creating a cron job.

To create a cron job, ensure you are running the terminal with root priviliges:

```bash
crontab -e
```

Ideally, we want to run our script once in the morning and once in the afternoon. We shall schedule our task to run at 0800 and 1400 everyday. We can do so using the following line:

```bash
0 8,14 * * * cd /path-to-directory/health-declaration-bot/ && python3 health_declaration.py
```

## Disclaimer

This project was embarked upon and completed for educational purposes. I do not condone dishonest declaration of health information, both when health declaration was mandatory within NUS and now. Should the Covid-19 Pandemic evolve or the emergence of any other national health emergency result in NUS reinstating mandatory health declaration, this project should not be used as a form of circumventing University policy. This project and its code is strictly for educational purposes only.

Temperature Declaration portal is now deprecated with Singapore and the Universities move towards living with Covid. However, this repo will remain up as a showcase of a personal project as well as for other looking to automate certain processes.

This is not the only open source iteration of the project available. I claim no credit for the inception and originality of such an idea.

I am not liable for any misuse or ill intentions as a result of running this script.
