# Contributing to Maker-Hub

Please take a moment to review this document in order to make the contribution
process easy and effective for everyone involved!

## Using the issue tracker

You can use the issues tracker for:

* [bug reports](#bug-reports)
* [feature requests](#feature-requests)
* [submitting pull requests](#pull-requests)

## Bug reports

A bug is a _demonstrable problem_ that is caused by the code in the repository.
Good bug reports are extremely helpful - thank you!

Guidelines for bug reports:

1. **Use the github issue search** &mdash; check if the issue has already been
   reported.

2. **Check if the issue has been fixed** &mdash; try to reproduce it using the
   `main` branch in the repository.

3. **Isolate and report the problem** &mdash; ideally create a reduced test
   case.

Please try to be as detailed as possible in your report. Include information about
your version of Maker-Hub and the OS you're using. Please provide steps to
reproduce the issue as well as the outcome you were expecting! Screen shots help!  All these details
will help developers to fix any potential bugs.

Example:

> Short and descriptive example bug report title
>
> A summary of the issue and the environment in which it occurs. If suitable,
> include the steps required to reproduce the bug.
>
> 1. This is the first step
> 2. This is the second step
> 3. Further steps, etc.
>
> Any other information you want to share that is relevant to the issue being
> reported. This might include the lines of code that you have identified as
> causing the bug, and potential solutions (and your opinions on their
> merits).

## Feature requests

Feature requests are welcome. But take a moment to find out whether your idea
fits with the scope and aims of the project. It's up to *you* to make a strong
case to convince the community of the merits of this feature.
Please provide as much detail and context as possible.

## Contributing Documentation

Project documentation is written in Markdown: it uses [mkdocs-material](https://squidfunk.github.io/mkdocs-material-insiders/)
formatting.

If possible include examples and screen shots.

## Pull requests

Good pull requests - patches, improvements, new features - are a fantastic
help. They should remain focused in scope and avoid containing unrelated
commits.

!!! Important
    By submitting a patch, you agree that your work will be
    licensed under the license used by the project.

If you have any large pull request in mind (e.g. implementing features,
refactoring code, etc), **please ask first** otherwise you risk spending
a lot of time working on something that the project's developers might
not want to merge into the project.

Please adhere to the coding conventions in the project (indentation,
accurate comments, etc.) and don't forget to add your own tests and
documentation. When working with git, we recommend the following process
in order to craft an excellent pull request:

1. [Fork](https://help.github.com/articles/fork-a-repo/) the project, clone your fork,
   and configure the remotes:

      ```sh
      # Clone your fork of the repo into the current directory
      git clone https://github.com/<your-username>/maker-hub
      # Navigate to the newly cloned directory
      cd maker-hub
      # Assign the original repo to a remote called "upstream"
      git remote add upstream https://github.com/madeinoz67/maker-hub
      ```

2. If you cloned a while ago, get the latest changes from upstream:

      ```bash
      git checkout master
      git pull upstream master
      ```

3. Create a new topic branch (off of `master`) to contain your feature, change,
   or fix.

   ```sh
      git checkout -b <topic-branch-name>
   ```

!!! Important
      Making changes in `master` is discouraged. You should always
      keep your local `master` in sync with upstream `master` and make your
      changes in topic branches.

4. Commit your changes in logical chunks. Keep your commit messages organized,
   with a short description in the first line and more detailed information on
   the following lines. Feel free to use Git's
   [interactive rebase](https://help.github.com/articles/about-git-rebase/)
   feature to tidy up your commits before making them public.

5. Push your topic branch up to your fork:
   
      ```sh
      git push origin <topic-branch-name>
      ```

6. [Open a Merge Request](https://help.github.com/articles/using-pull-requests/)
    with a clear title and description.

7. If you haven't updated your pull request for a while, you should consider
   rebasing on main and resolving any conflicts.
   
      ```sh
      git checkout master
      git pull upstream master
      git checkout <your-topic-branch>
      git rebase master
      ```

!!! Important
      _Never ever_ merge upstream `master` into your branches. You
      should always `git rebase` on `master` to bring your changes up to date when
      necessary.

Thank you for your contributions!
