# this will contain all the things related to Day 1 of the project

1. Created an env using `conda create -n dvc_versioning  python=3.9`.
2. Activated into the env.
3. Using commands from the offical site "https://dvc.org/doc/install/linux" installing dvc package:
    1. using pip
        1. `python -m pip install dvc` to install using pip.
        1. this works fine.
            <details>
                <summary> Success installation message </summary>
                Building wheels for collected packages: antlr4-python3-runtime
                Building wheel for antlr4-python3-runtime (setup.py) ... done
                Created wheel for antlr4-python3-runtime: filename=antlr4_python3_runtime-4.9.3-py3-none-any.whl size=144554 sha256=853dcee2042b2edd55483d775bad7cff8db931aebe1e4992b1829b6ce498147e
                Stored in directory: /home/prabin_nayak/.cache/pip/wheels/23/cf/80/f3efa822e6ab23277902ee9165fe772eeb1dfb8014f359020a
                Successfully built antlr4-python3-runtime
                Installing collected packages: wcwidth, pygtrie, funcy, dictdiffer, appdirs, antlr4-python3-runtime, zc.lockfile, voluptuous, vine, urllib3, tzdata, typing-extensions, tqdm, tomlkit, tabulate, smmap, six, shtab, shortuuid, shellingham, semver, ruamel.yaml.clib, PyYAML, pyparsing, pygments, pycparser, psutil, prompt-toolkit, platformdirs, pathspec, packaging, orjson, networkx, multidict, mdurl, idna, fsspec, frozenlist, filelock, entrypoints, dvc-render, dpath, distro, diskcache, colorama, click, charset-normalizer, certifi, billiard, attrs, atpublic, async-timeout, annotated-types, yarl, sqltrie, ruamel.yaml, requests, python-dateutil, pydot, pydantic-core, omegaconf, markdown-it-py, grandalf, gitdb, flufl.lock, flatten-dict, dvc-objects, dulwich, configobj, click-repl, click-plugins, click-didyoumean, cffi, amqp, aiosignal, rich, pygit2, pydantic, kombu, iterative-telemetry, hydra-core, gitpython, dvc-studio-client, dvc-data, cryptography, aiohttp, typer, celery, asyncssh, aiohttp-retry, scmrepo, dvc-task, dvc-http, gto, dvc
                Successfully installed PyYAML-6.0.1 aiohttp-3.9.5 aiohttp-retry-2.8.3 aiosignal-1.3.1 amqp-5.2.0 annotated-types-0.7.0 antlr4-python3-runtime-4.9.3 appdirs-1.4.4 async-timeout-4.0.3 asyncssh-2.14.2 atpublic-4.1.0 attrs-23.2.0 billiard-4.2.0 celery-5.4.0 certifi-2024.2.2 cffi-1.16.0 charset-normalizer-3.3.2 click-8.1.7 click-didyoumean-0.3.1 click-plugins-1.1.1 click-repl-0.3.0 colorama-0.4.6 configobj-5.0.8 cryptography-42.0.7 dictdiffer-0.9.0 diskcache-5.6.3 distro-1.9.0 dpath-2.1.6 dulwich-0.22.1 dvc-3.50.2 dvc-data-3.15.1 dvc-http-2.32.0 dvc-objects-5.1.0 dvc-render-1.0.2 dvc-studio-client-0.20.0 dvc-task-0.4.0 entrypoints-0.4 filelock-3.14.0 flatten-dict-0.4.2 flufl.lock-7.1.1 frozenlist-1.4.1 fsspec-2024.5.0 funcy-2.0 gitdb-4.0.11 gitpython-3.1.43 grandalf-0.8 gto-1.7.1 hydra-core-1.3.2 idna-3.7 iterative-telemetry-0.0.8 kombu-5.3.7 markdown-it-py-3.0.0 mdurl-0.1.2 multidict-6.0.5 networkx-3.2.1 omegaconf-2.3.0 orjson-3.10.3 packaging-24.0 pathspec-0.12.1 platformdirs-3.11.0 prompt-toolkit-3.0.43 psutil-5.9.8 pycparser-2.22 pydantic-2.7.1 pydantic-core-2.18.2 pydot-2.0.0 pygit2-1.15.0 pygments-2.18.0 pygtrie-2.5.0 pyparsing-3.1.2 python-dateutil-2.9.0.post0 requests-2.32.2 rich-13.7.1 ruamel.yaml-0.18.6 ruamel.yaml.clib-0.2.8 scmrepo-3.3.5 semver-3.0.2 shellingham-1.5.4 shortuuid-1.0.13 shtab-1.7.1 six-1.16.0 smmap-5.0.1 sqltrie-0.11.0 tabulate-0.9.0 tomlkit-0.12.5 tqdm-4.66.4 typer-0.12.3 typing-extensions-4.11.0 tzdata-2024.1 urllib3-2.2.1 vine-5.1.0 voluptuous-0.14.2 wcwidth-0.2.13 yarl-1.9.4 zc.lockfile-3.0.post1
            </details>            
    1. using conda ( didn't work )
        1. `conda install -c conda-forge mamba` first installing mamba for faster installation of dvc.
            Getting the following error:
            ```python
            (dvc_versioning) prabin_nayak@DESKTOP-IUPLGMD:~/Workspace/side_projects/project-of-the-week$ conda install -c conda-forge mamba
            Collecting package metadata (current_repodata.json): done
            Solving environment: unsuccessful initial attempt using frozen solve. Retrying with flexible solve.
            Solving environment: unsuccessful attempt using repodata from current_repodata.json, retrying with next repodata source.
            Collecting package metadata (repodata.json): - Killed
            ```
1. Follow the [video](personal_copy_data_versioning_dvc) at part "essentials DVC commands".
    `NOTE`: the dvc add command should be done before executing git commands.
    1. Go to the project folder, first run `dvc init` even before the data is present once. (i skipped this step ). This is similar to how we run git init before starting the project. SO the sequence should be git init >> dvc init.
        `NOTE`: it is advisable to use dvc where the git file is present.
        ```error
        ERROR: failed to initiate DVC - /home/prabin_nayak/Workspace/side_projects/project-of-the-week/2024-05-22-DVC/Day1 is not tracked by any supported SCM tool (e.g. Git). Use `--no-scm` if you don't want to use any SCM or `--subdir` if initializing inside a subdirectory of a parent SCM repository.
        ```
        Other workaround is to use `--subdir`. For more info visit, link[1]
        For this tutorial let's keep it simple. We will try to put it in root git folder "project of teh week" where the `.git` file is present, in a new folder named "dvc_demo".
    1. created the src and data folder to use how dvc works.
    Sequence of commands executed
    ```shell
        git init # initiating the git related files
        dvc init  # initiating the dvc related files

        dvc add data/data.txt # adding the 1st version of the file to "dvc" 
        git add data/.gitignore data/data.txt.dvc # adding the chnages made in the dvc specfic files to track
        git add . # adding the files to the git tracking
        git commit -m "run dvc with data file>>tracking changes with git" # commiting the changes to the git as group
        git push origin <localBranchName>:<remoteBranchName> # pushing the changes to the git remote

        // Making changes in the data file.

        dvc add data/data.txt # pushing the NEW changes to the dvc tracking file
        git add data/data.txt.dvc # adding the chnages made in the dvc specfic files to track
        git commit -m "changing the data file>> dvc add >> git add"  # commiting the changes to the git as group

        git log # to go the previous versions, check th log, press q to get out of the log
        git checkout ed644ccb8f45924523fe469ad5dac4d1cebce29f ## get the hash and do the checkout, THIS ONLY GETS FILES RELATED TO THAT PARTICULAR COMMIT. And as we are not tracking the data.txt, so we have to do something else to get the data associated with this particular commit
        dvc checkout # this takes the hash from current data.txt.dvc and collects the data from the cache folder. And finally you see the data related to the hash you were looking for

        git status
        git push origin <localBranchName>:<remoteBranchName>

    ```


[1]: https://dvc.org/doc/command-reference/init#initializing-dvc-in-subdirectories