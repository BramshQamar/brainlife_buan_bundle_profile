# BrainLife BUAN Bundle Profile

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Computes BUAN bundle profiles for one subject with DIPY: assigns points of a recognised bundle to segments along a model bundle and samples an anatomical measure such as FA along them, saving CSV files.**

Implements the bundle-profile step of Bundle Analytics (BUAN): the model bundle (standard space) and the subject's recognised bundle (common space) define an assignment of points to no_disks segments, and the measure map is sampled on the subject's bundle in native space. Use it after bundle recognition to obtain along-tract profiles for group statistics. As committed, profiles.py on this branch has a syntax error and does not import json, and the registry parameter key is malformed, so the App is unlikely to run.

| | |
|---|---|
| 📥 **Inputs** | `neuro/track/trk` ×3 · `neuro/tensor` |
| 📤 **Outputs** | `raw` |
| 🐳 **Container** | `brainlife/dipy:1.1.1` |
| ⚙️ **Resources** | 1 CPUs |
| 🔗 **Run it** | [doi.org/10.25663/brainlife.app.540](https://doi.org/10.25663/brainlife.app.540) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `model_bundle` | `neuro/track/trk` | yes | Model bundle in standard space |
| `rec_bundle` | `neuro/track/trk` | yes | Subject's bundle in common space |
| `org_bundle` | `neuro/track/trk` | yes | Subject's bundle in native space |
| `metric` | `neuro/tensor` | yes | Anatomical measures such as FA. |

#### 📤 Outputs

| Output | Datatype | Description |
|---|---|---|
| `output` | `raw` | output directory |

<details>
<summary><b>⚙️ Parameters</b> (1)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `"no_disks": 100,` | number | `100` | The number of segments along the length of the tract. |

</details>

📚 **References used by this App:**
- Chandio BQ et al. Bundle analytics, a computational framework for investigating the shapes and profiles of brain pathways across populations. Scientific Reports 10:17149 (2020).
- Garyfallidis E et al. Dipy, a library for the analysis of diffusion MRI data. Frontiers in Neuroinformatics 8:8 (2014). [doi:10.3389/fninf.2014.00008](https://doi.org/10.3389/fninf.2014.00008)
- Avesani P et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

<!-- brainlife-app:end -->

This is a Brainlife App for generating BUAN bundle profile. 

## App Description

 The App creates bundle profiles of the pathways and saves the information in HDF5 files. This app implements bundle profiles method presented in Bundle analytics, a computational framework for investigating the shapes and profiles of brain pathways across populations paper [1].

## Authors

[Bramsh Chandio](https://github.com/BramshQamar)

### Funding Acknowledgement
DIPY is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the software. We kindly ask that you acknowledge the funding below in your publications and code reusing this code.

[![NIH-NIBIB-R01EB027585](https://img.shields.io/badge/NIH_NIBIB-R01EB027585-green.svg)](https://grantome.com/grant/NIH/R01-EB027585-01)
[![NIH-NIMH-RF1MH121868](https://img.shields.io/badge/NIH_NIMH-RF1MH121868-green.svg)](https://grantome.com/grant/NIH/RF1-MH121868-01)
[![NIH-NIMH-R01MH108467](https://img.shields.io/badge/NIH_NIMH-R01MH108467-green.svg)](https://grantome.com/grant/NIH/R01-MH108467-01)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-EEC-1720625](https://img.shields.io/badge/NSF_BCS-1720625-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1720625)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)

## Citations

[1] Chandio, BQ., et al. Bundle analytics, a computational framework for investigating the shapes and profiles of brain pathways across populations. Scientific reports,  10, 17149 (2020).

## Running the App

#### 1. On Brainlife.io

You can see a list of [Dipy Apps currently regsitered on Brainlife](https://brainlife.io/apps#dipy). Find the App that you'd like to run and click "Execute" tab to specify dataset that you'd like to run the App on.

#### 2. On  your machine (Running Locally)

To run this command, you can simply type:

`singularity exec -e docker://brainlife/dipy:1.1.1 brainlife_buan_bundle_profile [your_args]`

To see the documentation of all arguments, [go to the following page](https://dipy.org/documentation/1.2.0./interfaces/buan_flow/)
```

## Input

To see the documentation of all the arguments, follow this [link](https://dipy.org/documentation/1.2.0./reference_cmd/dipy_buan_profiles/).

## Output

All output files will be generated according to the passed arguments, as explained [here](https://dipy.org/documentation/1.2.0./reference_cmd/dipy_buan_profiles/).
```
### Dependencies

This App requires [singularity](https://www.sylabs.io/singularity/) to run.

#### DIPY is licensed under the terms of the BSD license. Please see the [LICENSE file](https://github.com/dipy/dipy/blob/master/LICENSE).
