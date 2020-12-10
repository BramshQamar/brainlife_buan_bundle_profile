#!/usr/bin/env python3

import numpy as np
from dipy.workflows.stats import buan_bundle_profiles
import os
import json

if __name__ == '__main__':

    # Create Brainlife's output dirs if don't exist
    if not os.path.exists('output'):
        os.mkdir('output')

    # Read Brainlife's config.json
    with open('config.json', encoding='utf-8') as config_json:
        config = json.load(config_json)


    fname_bundles = config .get('model_bundles')
    fname_subject = config .get('subject')
    no_disks = config .get('no_disks')

    b = os.path.join(fname_subject, "rec_bundles")
    c = os.path.join(fname_subject, "org_bundles")
    d = os.path.join(fname_subject, "anatomical_measures")
    group_id = 0
    sub = fname_subject
    out_dir = 'output'
    buan_bundle_profiles(fname_bundles, b, c, d, group_id,
                         sub, no_disks, out_dir)
