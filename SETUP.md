# Publish Rahul's GitHub profile

This package is a GitHub profile README, not a separate hosted website. It has not been published to your account.

## 1. Preview

Open `PREVIEW.html` in a browser. It is an offline approximation of the README layout, with the same copy and artwork. GitHub controls its own typography, spacing, table layout, and light/dark appearance. The stats panels intentionally show “Awaiting first sync” until the workflow generates real data.

## 2. Add the files to your profile repository

Create or open the public repository `RahulAgarwal701/RahulAgarwal701`. GitHub displays its root `README.md` on your profile.

Copy these items to the repository root:

- `README.md`
- `assets/` (all five SVG files)
- `profile/` (all three starter SVG files)
- `scripts/update_stats.py`
- `.github/workflows/profile.yml`

The `.github` folder is hidden in macOS Finder; press **Command + Shift + .** to show it. Upload the extracted files, not the ZIP itself. If the browser uploader skips `.github`, use GitHub's **Add file → Create new file**, enter `.github/workflows/profile.yml` as the filename, and paste the supplied workflow.

For an existing repository, preserve your other files. Replace only the supplied README, artwork, stats script, and workflow paths. Keep your existing README in git history or a backup before replacing it.

`SETUP.md`, `DESIGN.md`, and `PREVIEW.html` are optional reference files. They are not necessary for the profile to render.

## 3. Generate the stats cards

Open the profile repository's **Actions** tab, select **Refresh profile graphics**, and select **Run workflow** on the default branch.

The first job fetches two SVGs from the original `anuraghazra/github-readme-stats` service and commits them to `profile/`. No personal token is required for these public cards. They refresh daily at approximately **7:53 AM IST** (02:23 UTC); GitHub may delay scheduled runs.

The service is best-effort and may be rate-limited. If it fails, the job reports the error and preserves the previous images. Before the first successful run, the honest pending panels remain. After success, your README displays real public activity and repository-language data. There are no fabricated counts, ranks, or language percentages.

The workflow requests `contents: write` only for the jobs that commit generated images. Repository or organization policies and branch protection may still prevent these commits. If Actions reports a push permission error, check the repository's Actions policy and branch rules. Do not disable unrelated protections.

## 4. Enable the lowlighter calendar

The isometric calendar needs a `METRICS_TOKEN` repository secret. The upstream plugin supports a classic GitHub personal access token with **no scopes** for public activity.

1. In your GitHub account settings, open **Developer settings → Personal access tokens → Tokens (classic)**.
2. Create an expiring token for this public profile calendar, leaving all scopes unchecked. If your account policy does not allow classic tokens, follow the upstream Metrics instructions for a supported alternative.
3. In `RahulAgarwal701/RahulAgarwal701`, go to **Settings → Secrets and variables → Actions → New repository secret**.
4. Name it `METRICS_TOKEN` and paste the token as the secret value. Never put it in the README, YAML file, or a chat message.
5. Rerun **Refresh profile graphics**. The calendar job writes `profile/calendar.svg`.

The separate automatic `GITHUB_TOKEN` handles the commit; the personal token is used to read public contribution data. Renew the secret when the token expires. Without it, only the calendar is skipped; the rest of the profile works.

The supplied workflow has been structurally checked but has not been executed against your GitHub account. First-run success depends on GitHub permissions, third-party availability, and the token above.

## 5. Finish your profile

Suggested bio:

> Building AI applications with Python | Generative AI, Computer Vision & Backend Systems

Location: `Pali, Rajasthan, India`

Pin your repositories in this order:

1. AutoRAG
2. Raya__LLM
3. Garbage_Detection
4. Outreach_Platform

For each pinned project, add a readable description, screenshot/demo, quick-start instructions, and a short account of what is implemented. Label measured benchmarks with dataset and hardware context.

## Content notes

- Education, internships, credentials, and project summaries come from your supplied resume and conversation. Your repository URLs could not be independently opened in this session; verify that they are public and spelled correctly.
- The credential links are the Google Drive URLs you supplied; they are labeled “Credential link,” not independent certification verification.
- The fictional internship figures discussed earlier are not used anywhere in this profile.
- MaterialGuard is not presented as a completed project or internship deliverable.
- “Waste Vision” and “AI Outreach” are short display labels; the links point to your original Garbage_Detection and Outreach_Platform repositories.
- GitHub strips arbitrary CSS and JavaScript from README HTML. The design uses SVG images, standard links, tables, and collapsible details that fit GitHub's README model.

## Sources and integrations

- [GPRM](https://github.com/VishwaGauravIn/github-profile-readme-maker): social badges and skills/component inspiration. Its visual builder was unavailable, so no generator export is claimed.
- [GitHub Readme Stats](https://github.com/anuraghazra/github-readme-stats): original public stats and languages SVG endpoints, cached by the included Python script.
- [lowlighter/metrics](https://github.com/lowlighter/metrics): actual GitHub Action integration for the isometric contribution calendar.
- [Awesome GitHub Profile README](https://github.com/abhisheknaiidu/awesome-github-profile-readme): inspiration from its Minimalistic, Code Mode, and GitHub Actions categories. No contributor's profile was copied.
- [GitHub profile README documentation](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme)
- [Metrics calendar documentation](https://github.com/lowlighter/metrics/tree/master/source/plugins/isocalendar)

## Troubleshooting

**Images are broken:** ensure the assets and profile folders are in the same repository root as README.md; file names are case-sensitive.

**Stats are still pending:** run the workflow manually and inspect the stats job. A network/provider error retains the starter card until a later successful run.

**Calendar is still pending:** check the secret name, expiration, and calendar job log. An empty secret skips that step intentionally.

**The page looks different in GitHub's light theme:** only the SVG panels have a fixed dark background. Surrounding text follows GitHub's theme. That is expected.

**Workflow isn't visible:** verify `.github/workflows/profile.yml` was uploaded to the default branch, not inside an extra `rahul-github-profile/` folder.
