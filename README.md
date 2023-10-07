# University Logo for ICPC scoreboard

This repository contains logo of universities that are participating in ICPC Vietnam.

This repository is to help show the logo of universities instead of their names in the scoreboard!

See demo [here](https://icpcvn.github.io/2022/regional/scoreboard.html).

## How to contribute

- First, check if your university logo is already in the repository, try to find it in the [list of universities](data.json).
- If your university logo is not in the repository (or the logo is not correct, not in high quality, ...), you can contribute by adding it to the repository by following the steps below:
  - Fork this repository.
  - Add/replace your university logo to the [logos](logos) folder.
  - Add/replace your university to the [list of universities](data.json) in the following format:
    ```json
    {
      "name": "University Name",
      "logo": "<id>.png"
    }
    ```
    where `<id>.png` is the name of your university logo file.
  - Commit and push your changes to your forked repository.
  - Create a pull request to this repository.

## Preferred logo format

- The logo should be square.
- The logo should be at least 50x50 pixels, at most 1000x1000 pixels. The preferred size is 200x200 pixels.
- The logo should have transparent background and in PNG format.
