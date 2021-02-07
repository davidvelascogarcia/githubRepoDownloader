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
from halo import Halo
import platform


class GithubRepoDownloader:

    # Function: Constructor
    def __init__(self):

        # Build Halo spinner
        self.systemResponse = Halo(spinner='dots')

    # Function: getSystemPlatform
    def getSystemPlatform(self):

        # Get system configuration
        print("\nDetecting system and release version ...\n")
        systemPlatform = platform.system()
        systemRelease = platform.release()

        print("**************************************************************************")
        print("Configuration detected:")
        print("**************************************************************************")
        print("\nPlatform:")
        print(systemPlatform)
        print("Release:")
        print(systemRelease)

        return systemPlatform, systemRelease

    # Function: getUser
    def getUser(self):

        print("**************************************************************************")
        print("Enter username")
        print("**************************************************************************")

        systemResponseMessage = "\n[INFO] Please, enter username:\n"
        self.systemResponse.text_color = "blue"
        self.systemResponse.info(systemResponseMessage)

        # Get username
        githubUsername = input()

        return githubUsername

    # Function: repoDownloader
    def repoDownloader(self, githubUsername):

        # Get initial time
        initialTime = datetime.datetime.now()

        print("\n**************************************************************************")
        print("Searching Repositories")
        print("**************************************************************************")

        systemResponseMessage = "\n[INFO] Searching " + str(githubUsername) + " repositories ...\n"
        self.systemResponse.text_color = "yellow"
        self.systemResponse.warn(systemResponseMessage)

        # Create github client and get username repos
        try:
            # Build githubClient
            githubClient = Github()

            # Get github user profile
            githubUser = githubClient.get_user(str(githubUsername))

            # Get githubUser repositories list
            githubUserRepos = githubUser.get_repos()

        except:

            systemResponseMessage = "\n[ERROR] Error getting github user repositories.\n"
            self.systemResponse.text_color = "red"
            self.systemResponse.fail(systemResponseMessage)

        # Move to root path
        try:
            os.chdir("./../../")

        except:

            systemResponseMessage = "\n[ERROR] Error moving to root path.\n"
            self.systemResponse.text_color = "red"
            self.systemResponse.fail(systemResponseMessage)

        # Variable to count repo downloaded
        repoDownloadedCount = 1

        # Download all user repositories
        for repo in githubUserRepos:

            systemResponseMessage = "\n[INFO] Repo founded: " + str(repo.name) + "\n"
            self.systemResponse.text_color = "yellow"
            self.systemResponse.warn(systemResponseMessage)

            # Execute repo clone
            try:
                print("\n**************************************************************************")
                print("Downloading repo " + str(repo.name))
                print("**************************************************************************\n")

                systemResponseMessage = "\n[INFO] Downloading repo " + str(repo.name) + ", " + str(repoDownloadedCount) + "/" + str(githubUserRepos.totalCount) + " ...\n"
                self.systemResponse.text_color = "blue"
                self.systemResponse.info(systemResponseMessage)

                # Prepare github repo path and clone command
                githubRepoPath = "https://github.com/" + str(githubUsername) + "/" + str(repo.name)
                cloneCommand = "git clone " + str(githubRepoPath)

                os.system(str(cloneCommand))

                systemResponseMessage = "\n[INFO] " + str(repo.name) + " repo cloned correctly.\n"
                self.systemResponse.text_color = "green"
                self.systemResponse.succeed(systemResponseMessage)

            except:
                os.system(str(cloneCommand))

                systemResponseMessage = "\n[ERROR] Error cloning " + str(repo.name) + " repo.\n"
                self.systemResponse.text_color = "red"
                self.systemResponse.fail(systemResponseMessage)

            # Count repoDownloadedCount + 1
            repoDownloadedCount = repoDownloadedCount + 1

        print("\n**************************************************************************")
        print(str(githubUsername) + " Repositories Cloned")
        print("**************************************************************************")

        systemResponseMessage = "\n[INFO] " + str(githubUsername) + " repositories cloned correctly.\n"
        self.systemResponse.text_color = "green"
        self.systemResponse.succeed(systemResponseMessage)

        # Get end time
        endTime = datetime.datetime.now()

        # Get elapsedTime
        elapsedTime = endTime - initialTime

        systemResponseMessage = "\n[INFO] Elapsed time: " + str(elapsedTime)
        self.systemResponse.text_color = "blue"
        self.systemResponse.info(systemResponseMessage)


# Function: main
def main():

    print("**************************************************************************")
    print("**************************************************************************")
    print("                   Program: Github Repo Downloader                        ")
    print("                     Author: David Velasco Garcia                         ")
    print("                             @davidvelascogarcia                          ")
    print("**************************************************************************")
    print("**************************************************************************")

    print("\nLoading Github Repo Downloader engine ...\n")

    # Build githubRepoDownloader object
    githubRepoDownloader = GithubRepoDownloader()

    # Get system platform
    systemPlatform, systemRelease = githubRepoDownloader.getSystemPlatform()

    # Set Github username
    username = githubRepoDownloader.getUser()

    # Get Github repos
    githubRepoDownloader.repoDownloader(username)

    print("\n**************************************************************************")
    print("Program finished:")
    print("**************************************************************************")
    print("\ngithubRepoDownloader program finished correctly.\n")

    userExit = input()

if __name__ == "__main__":

    # Call main function
    main()
