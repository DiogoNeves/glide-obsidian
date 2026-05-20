# Release Privacy Checklist

Use this before publishing Glide.

## Working Tree

- No private names, emails, phone numbers, addresses, company names, family details, health details, financial details, app account details, or private project data.
- No copied personal notes.
- No absolute local paths.
- No secrets, tokens, API keys, cookies, or credentials.
- `LICENSE` uses neutral contributor attribution.
- README privacy language says Glide does not collect data and harness privacy depends on configuration.

Suggested scan:

```sh
rg -n -i "e[m]ail|g[m]ail|address|token|secret|password|api[_-]?key|priv[a]te|family|client|/[U]sers/" .
```

Add project-specific terms before release.

## Git History

Do not publish history containing private content or personal author metadata.

If history is not clean, create a fresh history with neutral author metadata before pushing to a public remote.

Suggested verification:

```sh
git log --format='%h %an <%ae> %s' --all
git grep -n -I -i "priv[a]te\\|secret\\|token\\|/[U]sers/" $(git rev-list --all)
```

Review the output manually.

## Distribution

- Public repo remote is correct.
- No old private remote remains.
- Release branch is built from the clean history.
- Installer docs tell users not to overwrite existing vault files without confirmation.
