'''
  * ***************************************************************
  *      Program: Github Repo Downloader
  *      Type: Python
  *      Author: David Velasco Garcia @davidvelascogarcia
  * ***************************************************************
'''

# Libraries
import datetime
from github import Github
import os
import platform
import sys
import time

print("")
print("")
print("**************************************************************************")
print("**************************************************************************")
print("                   Program: Github Repo Downloader                        ")
print("                     Author: David Velasco Garcia                         ")
print("                             @davidvelascogarcia                          ")
print("**************************************************************************")
print("**************************************************************************")

print("")
print("Starting system ...")
print("")

print("")
print("Loading githubRepoDownloader engine ...")
print("")

# Get system configuration
print("")
print("Detecting system and release version ...")
print("")
systemPlatform = platform.system()
systemRelease = platform.release()

print("")
print("**************************************************************************")
print("Configuration detected:")
print("**************************************************************************")
print("")
print("Platform:")
print(systemPlatform)
print("Release:")
print(systemRelease)

# Get initial time
initialTime = datetime.datetime.now()

print("")
print("**************************************************************************")
print("Enter username")
print("**************************************************************************")
print("")
print("[INFO] Please, enter username:")
print("")

# Get username
githubUsername = input("Username: ")

print("")
print("**************************************************************************")
print("Searching Repositories")
print("**************************************************************************")
print("")
print("[INFO] Searching " + str(githubUsername) + " repositories ...")
print("")

# Create github client and get username repos
try:
    # Build githubClient
    githubClient = Github()

    # Get github user profile
    githubUser = githubClient.get_user(str(githubUsername))

    # Get githubUser repositorieslist
    githubUserRepos = githubUser.get_repos()

except:
    print("")
    print("[ERROR] Error getting github user repositories.")
    print("")

    # Move to root path
try:
    os.chdir("./../../")

except:
    print("")
    print("[ERROR] Error moving to root path.")
    print("")

# Variable to count repo downloaded
repoDownloadedCount = 1

# Download all user repositories
for repositorie in githubUserRepos:

    print("")
    print("[INFO] Repositorie founded: " + str(repositorie.name))
    print("")

    print("")
    print("**************************************************************************")
    print("Downloading repositorie " + str(repositorie.name))
    print("**************************************************************************")
    print("")
    print("[INFO] Downloading repositorie " + str(repositorie.name) + ", " + str(repoDownloadedCount) + "/" + str(githubUserRepos.totalCount) + " ...")
    print("")

    # Prepare github repositorie path
    githubRepoPath = "https://github.com/" + str(githubUsername) + "/" + str(repositorie.name)

    # Prepare cloneCommand
    cloneCommand = "git clone " + str(githubRepoPath)

    # Execute repositorie clone
    try:
        os.system(str(cloneCommand))

        print("")
        print("[INFO] " + str(repositorie.name) + " repositorie cloned correctly.")
        print("")

    except:
        print("")
        print("[ERROR] Error cloning " + str(repositorie.name) + " repositorie.")
        print("")

    # Count repoDownloadedCount + 1
    repoDownloadedCount = repoDownloadedCount + 1

print("")
print("**************************************************************************")
print(str(githubUser) + " Repositories Cloned")
print("**************************************************************************")
print("")
print("[INFO] " + str(githubUser) + " repositories cloned correctly.")
print("")

# Get end time
endTime = datetime.datetime.now()

# Get elapsedTime
elapsedTime = endTime - initialTime

print("")
print("[INFO] Elapsed time: " + str(elapsedTime))
print("")

print("")
print("")
print("**************************************************************************")
print("Program finished")
print("**************************************************************************")
print("")
print("githubRepoDownloader program finished correctly. ")
print("")
endProgram = input()
