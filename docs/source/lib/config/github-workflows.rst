Github Workflows
================

.. highlight:: hy

Github actions can be automated with Antilisp. Here is a script to generate a workflow with Antilisp::

    ; example from https://docs.github.com/en/actions/writing-workflows/quickstart


    (def (echo text)
         ; (sum) uses the object-oriented (+) and supports any type for which (+) is defined
         (sum
           (list
             "echo "
             (yaml-quote text))))
    ;(print (echo "message"))
    ; -> echo "message"


    (save-workflow ".github/workflows/github-actions-demo.yml"
      (workflow "GitHub Actions Demo" "push"
                ;; the run-name field is not implemented in the library:
                ;'run-name "${{ github.actor }} is testing out GitHub Actions 🚀"

                ; declare the jobs
                (job "Explore-GitHub-Actions" "ubuntu-latest"
                     ; as you can see, the syntax is very easy to understand
                     (run "echo \"🎉 The job was automatically triggered by a ${{ github.event_name }} event.\"")
                     ; but escaping quotes to nest the echo parameter is annoying
                     (run "echo \"🐧 This job is now running on a ${{ runner.os }} server hosted by GitHub!\"")
                     ; let's abstract it:
                     (run (echo "🔎 The name of your branch is ${{ github.ref }} and your repository is ${{ github.repository }}."))
                     (use
                       ; optional fields can be set with keyword (named) arguments
                       'name "Check out repository code"
                       "actions/checkout@v4")
                     (run (echo "💡 The ${{ github.repository }} repository has been cloned to the runner."))
                     (run (echo "🖥️ The workflow is now ready to test your code on the runner."))
                     (run
                       'name "List files in the repository"
                       "ls ${{ github.workspace }}")
                     (run (echo "🍏 This job's status is ${{ job.status }}.")))))


This example is taken from the yaml example in the Github Actions documentation and gives the following result:

.. highlight:: yaml

::

    name: GitHub Actions Demo
    on: [push]
    jobs:
      Explore-GitHub-Actions:
        runs-on: ubuntu-latest
        steps:
          - run: "echo "🎉 The job was automatically triggered by a ${{ github.event_name }} event.""
          - run: "echo "🐧 This job is now running on a ${{ runner.os }} server hosted by GitHub!""
          - run: "echo "🔎 The name of your branch is ${{ github.ref }} and your repository is ${{ github.repository }}.""
          - uses: "actions/checkout@v4"
            name: "Check out repository code"
          - run: "echo "💡 The ${{ github.repository }} repository has been cloned to the runner.""
          - run: "echo "🖥️ The workflow is now ready to test your code on the runner.""
          - run: "ls ${{ github.workspace }}"
          - run: "echo "🍏 This job's status is ${{ job.status }}.""
