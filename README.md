<a href="https://www.ultralytics.com/"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

# 🎉 Introduction

Welcome to the Ultralytics WAVE repository! This directory contains innovative code developed by Ultralytics for **WA**veform **V**ector **E**xploitation, focusing on particle physics detector readout and reconstruction. Our work leverages cutting-edge [Machine Learning (ML)](https://www.ultralytics.com/glossary/machine-learning-ml) and [Deep Neural Networks (DNNs)](https://www.ultralytics.com/glossary/deep-learning-dl) to enhance data analysis.

This software is available for use and redistribution under the **AGPL-3.0 license**. For a comprehensive overview of our projects and solutions, please visit [Ultralytics](https://www.ultralytics.com/).

[![Ultralytics Actions](https://github.com/ultralytics/sandd/actions/workflows/format.yml/badge.svg)](https://github.com/ultralytics/sandd/actions/workflows/format.yml)
[![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics)
[![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com/)
[![Ultralytics Reddit](https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue)](https://reddit.com/r/ultralytics)

# 📜 Description

The [Ultralytics WAVE repository](https://github.com/ultralytics/wave) offers a novel approach to particle physics detector readout and reconstruction through **WA**veform **V**ector **E**xploitation. By utilizing advanced ML and DNN techniques, WAVE aims to improve the precision and efficiency of interpreting complex waveform data from Time-Of-Flight detectors, contributing to advancements in [AI research](https://www.ultralytics.com/blog/the-role-of-deep-research-models-in-ai-advancements).

# 📦 Requirements

To get started with WAVE, you'll need [Python](https://www.python.org/) 3.7 or newer. The necessary libraries can be easily installed using `pip` and the provided `requirements.txt` file:

```bash
pip3 install -U -r requirements.txt
```

Key package requirements include:

- `numpy`: Fundamental package for numerical computation.
- `scipy`: Used for scientific and technical computing tasks.
- `torch` (version 0.4.0+): An open-source ML framework for building and training neural networks.
- `tensorflow` (version 1.8.0+): A comprehensive ecosystem for ML, offering tools, libraries, and community resources.
- `plotly` (optional): For creating interactive data visualizations.

You can find more information about these tools on their respective websites: [NumPy](https://numpy.org/), [SciPy](https://scipy.org/), [PyTorch](https://pytorch.org/), [TensorFlow](https://www.tensorflow.org/), and [Plotly](https://plotly.com/python/).

# 🚀 Running the Code

Several scripts are available to execute the WAVE models:

- **PyTorch Implementation**: Use `wave_pytorch.py` for models developed with the PyTorch framework.
- **TensorFlow Implementation**: Run `wave_tf.py` for models based on TensorFlow.
- **PyTorch on Google Cloud Platform**: Deploy `wave_pytorch_gcp.py` for running PyTorch models within the [Google Cloud Platform (GCP)](https://cloud.google.com/) environment.

# ✨ Visualizations

Here are some example visualizations showcasing waveforms processed by WAVE and the training progress of the models:

![](https://github.com/ultralytics/wave/blob/main/data/waveforms.png "Waveforms") ![](https://github.com/ultralytics/wave/blob/main/data/wave.png "Training Progress")

# 📄 Citation

If you utilize this project in your research or publications, we appreciate it if you cite our work. Please use the following citation format:

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

We actively welcome contributions from the open-source community! Whether it's fixing bugs, adding new features, or improving documentation, your help is valuable. Please see our [Contributing Guide](https://docs.ultralytics.com/help/contributing/) for more details on how to get started.

We also encourage you to share your experiences with Ultralytics projects by filling out our [Survey](https://www.ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey). Your feedback helps us improve. A huge 🙏 thank you to all our contributors!

[![Ultralytics open-source contributors](https://raw.githubusercontent.com/ultralytics/assets/main/im/image-contributors.png)](https://github.com/ultralytics/ultralytics/graphs/contributors)

# ©️ License

Ultralytics provides two licensing options to accommodate different use cases:

- **AGPL-3.0 License**: This [OSI-approved](https://opensource.org/license/agpl-v3) open-source license is ideal for students, researchers, and enthusiasts who wish to collaborate and share knowledge openly. See the [LICENSE](https://github.com/ultralytics/ultralytics/blob/main/LICENSE) file for full details.
- **Enterprise License**: Designed for commercial applications, this license permits the integration of Ultralytics software and AI models into commercial products and services without the open-source requirements of AGPL-3.0. If your project requires an Enterprise License, please contact us through [Ultralytics Licensing](https://www.ultralytics.com/license).

# 📬 Contact Us

For bug reports, feature requests, and contributions, please visit [GitHub Issues](https://github.com/ultralytics/sandd/issues). For broader questions and discussions about WAVE or other Ultralytics projects, join our vibrant community on [Discord](https://discord.com/invite/ultralytics)!

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
