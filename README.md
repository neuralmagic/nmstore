# NM GitHub Actions

### Curated collection of commonly used GitHub Actions and workflows within Neural Magic's and vLLM's Processes

## Overview

This repository hosts a collection of GitHub Actions developed and maintained by Neural Magic. These actions aim to improve automation, CI/CD pipelines, and workflow orchestration. They are designed for performance, scalability, and ease of use and support a range of deployment, testing, and optimization workflows.

### Key Actions

- Coming soon

Each action supports various configurable arguments to tailor the workflows to your project needs.

## Getting Started

To start using one of our GitHub Actions, include the relevant action within your workflow configuration file:

```yaml
name: Example Workflow
on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout Code
      uses: actions/checkout@v2

    - name: ACTION
      uses: neuralmagic/nm-actions/ACTION@main
      with:
        config-file: .eslintrc
```

This example shows how to integrate an NM action into a workflow. Visit each action's README for more configuration options and examples.

## Development

To contribute to NM Public Actions, follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. `pip install tox` and run `tox -e quality` to ensure your changes meet the quality standards and `tox -e style` to enforce the style guide and formatting.
5. Submit a pull request.

## Resources

### Documentation

Each GitHub Action contains a `README.md` alongside any supporting documents. To learn more, dive into the action you'd like to use.

### Releases

Visit our [GitHub Releases page](https://github.com/neuralmagic/nm-actions/releases) and review the release notes to stay updated with the latest releases.

### License

NM Public Actions are licensed under the [Apache License 2.0](https://github.com/neuralmagic/guidellm/blob/main/LICENSE).

## Community

### Contribute

We appreciate contributions to the code, examples, integrations, documentation, bug reports, and feature requests! To contribute:

1. Fork the repository.
2. Make your changes.
3. Submit a pull request.

### Join

We invite you to join our growing community of developers, researchers, and enthusiasts passionate about LLMs and optimization. Whether you're looking for help, want to share your own experiences, or stay up to date with the latest developments, there are plenty of ways to get involved:

- [**Neural Magic Community Slack**](https://neuralmagic.com/community/) - Join our Slack channel to connect with other NM users and developers. Ask questions, share your work, and get real-time support.
- [**GitHub Issues**](https://github.com/neuralmagic/nm-actions/issues) - Report bugs, request features, or browse existing issues. Your feedback helps us improve.
- [**Subscribe to Updates**](https://neuralmagic.com/subscribe/) - Sign up for the latest news, announcements, and updates about NM Public Actions, webinars, events, and more.
- [**Contact Us**](http://neuralmagic.com/contact/) - Use our contact form for general questions about Neural Magic or NM Public Actions.
