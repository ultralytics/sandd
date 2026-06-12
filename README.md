<a href="https://www.ultralytics.com/"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

# 🎉 Introduction

Welcome to the Ultralytics SANDD repository! This directory contains experimental waveform analysis code developed by Ultralytics for particle physics detector readout and reconstruction. Our work leverages [Machine Learning (ML)](https://www.ultralytics.com/glossary/machine-learning-ml) and scientific Python tooling to enhance data analysis.

This software is available for use and redistribution under the **AGPL-3.0 license**. For a comprehensive overview of our projects and solutions, please visit [Ultralytics](https://www.ultralytics.com/).

[![Ultralytics Actions](https://github.com/ultralytics/sandd/actions/workflows/format.yml/badge.svg)](https://github.com/ultralytics/sandd/actions/workflows/format.yml)
[![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics)
[![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com/)
[![Ultralytics Reddit](https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue)](https://reddit.com/r/ultralytics)

# 📜 Description

This repository provides SANDD waveform-processing scripts for local detector data files. `train.py` reads `.glenn` waveform dumps, subtracts pedestals, computes timing and charge features, applies candidate cuts, and writes a `results.png` summary plot. `waveform_plot.py` plots a sample waveform from a ROOT file when [ROOT](https://root.cern/) and `root_numpy` are available.

# 📦 Requirements

To get started with WAVE, you'll need [Python](https://www.python.org/) 3.7 or newer. The necessary libraries can be easily installed using `pip` and the provided `requirements.txt` file:

```bash
pip3 install -U -r requirements.txt
```

Key package requirements include:

- `numpy`: Fundamental package for numerical computation.
- `scipy`: Used for scientific and technical computing tasks.
- `torch`: An open-source ML framework for building and training neural networks.
- `matplotlib`: Used for plotting waveform and charge-distribution summaries.

The optional `waveform_plot.py` script also requires CERN ROOT and `root_numpy`, as noted in `requirements.txt`. You can find more information about these tools on their respective websites: [NumPy](https://numpy.org/), [SciPy](https://scipy.org/), [PyTorch](https://pytorch.org/), [Matplotlib](https://matplotlib.org/), and [ROOT](https://root.cern/).

# 🚀 Running the Code

The current repository includes two local scripts:

- **Waveform Processing**: Run `python train.py` after updating the local `path` variable near the top of the script to point at your SANDD `.glenn` data directory.
- **Waveform Plotting**: Run `python waveform_plot.py` from a directory containing the expected ROOT input file after installing ROOT and `root_numpy`.

# ✨ Visualizations

The related Ultralytics WAVE project includes example waveform and training-progress visualizations:

![](https://github.com/ultralytics/wave/blob/main/data/waveforms.png "Waveforms") ![](https://github.com/ultralytics/wave/blob/main/data/wave.png "Training Progress")

# 📄 Citation

If the related WAVE methodology is useful in your research or publications, we appreciate it if you cite our work using the following format:

```bibtex
@misc{jocher2018wave,
      title={WAVE: Machine Learning for Full-Waveform Time-Of-Flight Detectors},
      author={Glenn Jocher and Kurt Nishimura and Jacob Koblanski and Victor Li},
      year={2018},
      eprint={1811.05875},
      archivePrefix={arXiv},
      primaryClass={physics.ins-det}
}
```

You can access the paper on [ArXiv.org](https://arxiv.org/abs/1811.05875).

# 🤝 Contribute

We actively welcome contributions from the open-source community! Whether it's fixing bugs, adding new features, or improving documentation, your help is valuable. Please see our [Contributing Guide](https://docs.ultralytics.com/help/contributing) for more details on how to get started.

We also encourage you to share your experiences with Ultralytics projects by filling out our [Survey](https://www.ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey). Your feedback helps us improve. A huge 🙏 thank you to all our contributors!

[![Ultralytics open-source contributors](https://raw.githubusercontent.com/ultralytics/assets/main/im/image-contributors.png)](https://github.com/ultralytics/sandd/graphs/contributors)

# ©️ License

Ultralytics provides two licensing options to accommodate different use cases:

- **AGPL-3.0 License**: This [OSI-approved](https://opensource.org/license/agpl-3.0) open-source license is ideal for students, researchers, and enthusiasts who wish to collaborate and share knowledge openly. See the [LICENSE](https://github.com/ultralytics/sandd/blob/main/LICENSE) file for full details.
- **Enterprise License**: Designed for commercial applications, this license permits the integration of Ultralytics software and AI models into commercial products and services without the open-source requirements of AGPL-3.0. If your project requires an Enterprise License, please contact us through [Ultralytics Licensing](https://www.ultralytics.com/license).

# 📬 Contact Us

For bug reports, feature requests, and contributions, please visit [GitHub Issues](https://github.com/ultralytics/sandd/issues). For broader questions and discussions about SANDD or other Ultralytics projects, join our vibrant community on [Discord](https://discord.com/invite/ultralytics)!

<br>
<div align="center">
  <a href="https://github.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="3%" alt="Ultralytics GitHub"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.linkedin.com/company/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="3%" alt="Ultralytics LinkedIn"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://twitter.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png" width="3%" alt="Ultralytics Twitter"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://youtube.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="3%" alt="Ultralytics YouTube"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.tiktok.com/@ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="3%" alt="Ultralytics TikTok"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://ultralytics.com/bilibili"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-bilibili.png" width="3%" alt="Ultralytics BiliBili"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://discord.com/invite/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="3%" alt="Ultralytics Discord"></a>
</div>
