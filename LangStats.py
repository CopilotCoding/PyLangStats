from github import Github

# Replace YOUR_TOKEN with your Github API token
g = Github("YOUR_TOKEN")

# Replace YOUR_USERNAME with the username of the user you want to fetch the statistics for
user = g.get_user("YOUR_USERNAME")

# Get all the public repositories of the user
repos = user.get_repos(type='public')

# Initialize a dictionary to store the language statistics
language_stats = {}

# Loop through each repository and get the language statistics
for repo in repos:
    if not repo.fork:
        languages = repo.get_languages()
        for language in languages:
            if language in language_stats:
                language_stats[language] += languages[language]
            else:
                language_stats[language] = languages[language]

# Calculate the total number of bytes
total_bytes = sum(language_stats.values())

# Calculate the percentage of each language
for language in language_stats:
    language_stats[language] = "{:.4f}%".format(language_stats[language] / total_bytes * 100)

# Print the language statistics as percentages
print(language_stats)
