#!/bin/bash
echo "Checkouting all the modules to version "$1", or the most closest minor release to it."

target_version=$1

# Validate version
version_re_pattern=[0-9]\.[0-9]
if [[ ! $target_version =~ $version_re_pattern ]]; then
    echo "Error: Version should be like 3.8, i.e. two digits separated by a dot."
    return
fi

# Go to the modules directory
cd ../trytond/trytond/modules/

# Loop through all the modules
for m in $( ls -d */ ); do
    echo ${m:: -1}
    cd $m

    # Check if we are already on the desired branch/version
    if [[ ! `git rev-parse --abbrev-ref HEAD` = $target_version ]]; then

        # Checkout to the needed version
        if [[ `git ls-remote --heads origin $target_version` ]]; then
            git checkout $target_version  >/dev/null 2>&1
        else
            echo "  Warning: Exact version match was not found, looking for some previous minor release. Stable working is not guaranteed."
            found=0
            for v in `seq ${target_version: -1} -1 0`; do
                version=${target_version:: -1}$v
                if [[ `git ls-remote --heads origin $version` ]]; then
                    git checkout $version  >/dev/null 2>&1
                    found=1
                    break
                fi
            done
            if [[ $found = 0 ]]; then echo "  Error: No suitable version was found!"; fi
        fi
    fi

    echo "  `git rev-parse --abbrev-ref HEAD`"
    cd ..
done

cd ../../../trytond_scripts
