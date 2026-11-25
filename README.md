<h1 align="center">BUAN Bundle Profiles</h1>

<p align="center">
  Computes BUAN bundle profiles for one subject with DIPY: assigns points of a recognised bundle to segments along a model bundle and samples an anatomical measure such as FA along them, saving CSV files.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.540"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.540-blue.svg" alt="Run on brainlife.io"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Computes BUAN bundle profiles for one subject with DIPY: assigns points of a recognised bundle to segments along a model bundle and samples an anatomical measure such as FA along them, saving CSV files.**

Implements the bundle-profile step of Bundle Analytics (BUAN): the model bundle (standard space) and the subject's recognised bundle (common space) define an assignment of points to no_disks segments, and the measure map is sampled on the subject's bundle in native space. Use it after bundle recognition to obtain along-tract profiles for group statistics. As committed, profiles.py on this branch has a syntax error and does not import json, and the registry parameter key is malformed, so the App is unlikely to run.

| | |
|---|---|
| **Inputs** | `neuro/track/trk` ×3 · `neuro/tensor` |
| **Outputs** | `raw` |
| **Container** | `brainlife/dipy:1.1.1` |
| **Resources** | 1 CPUs |
| **Run it** | [doi.org/10.25663/brainlife.app.540](https://doi.org/10.25663/brainlife.app.540) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `model_bundle` | `neuro/track/trk` | yes | Model bundle in standard space |
| `rec_bundle` | `neuro/track/trk` | yes | Subject's bundle in common space |
| `org_bundle` | `neuro/track/trk` | yes | Subject's bundle in native space |
| `metric` | `neuro/tensor` | yes | Anatomical measures such as FA. |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `output` | `raw` | output directory |

<details>
<summary><b>Parameters</b> (1)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `"no_disks": 100,` | number | `100` | The number of segments along the length of the tract. |

</details>

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.540](https://doi.org/10.25663/brainlife.app.540), choose `neuro/track/trk`, `neuro/track/trk`, `neuro/track/trk`, `neuro/tensor` from your project, set the parameters and press **Execute**. The results are saved to your project as `raw`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `brainlife/dipy:1.1.1`), [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "model_bundle": "/path/to/model_bundle/model_bundle",
       "rec_bundle": "/path/to/rec_bundle/rec_bundle",
       "org_bundle": "/path/to/org_bundle/org_bundle",
       "measure": "/path/to/metric/measure",
       "\"no_disks\": 100,": 100
   }
   ```

3. Run `./main`.

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- BUAN Bundle Profiles. brainlife.io App. [doi:10.25663/brainlife.app.540](https://doi.org/10.25663/brainlife.app.540)
- Chandio BQ et al. Bundle analytics, a computational framework for investigating the shapes and profiles of brain pathways across populations. Scientific Reports 10:17149 (2020).
- Garyfallidis E et al. Dipy, a library for the analysis of diffusion MRI data. Frontiers in Neuroinformatics 8:8 (2014). [doi:10.3389/fninf.2014.00008](https://doi.org/10.3389/fninf.2014.00008)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

[Bramsh Chandio](https://github.com/BramshQamar)

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io, which runs this App, is publicly funded by Wellcome, the U.S. National Institutes of Health and the U.S. National Science Foundation; acknowledging that support helps keep it running.</sub>
