import os
import numpy as np
from scipy.ndimage.interpolation import map_coordinates
from dipy.utils.optpkg import optional_package
from dipy.tracking.streamline import transform_streamlines
from dipy.io.streamline import load_tractogram
from dipy.stats.analysis import assignment_map
from dipy.io.image import load_nifti
from time import time
import sys

pd, have_pd, _ = optional_package("pandas")
_, have_tables, _ = optional_package("tables")

def save_buan_profiles_csv(fname, dt):
    """ Saves the given input dataframe to .csv file

    Parameters
    ----------
    fname : string
        file name for saving the csv file
    dt : Pandas DataFrame
        DataFrame to be saved as .csv file

    """

    df = pd.DataFrame(dt)
    filename_hdf5 = fname + '.csv'

    df.to_csv(filename_hdf5, mode='a', header=False)



def anatomical_measures(bundle, metric, dt, pname, ind, dir):
    """ Calculates dti measure (eg: FA, MD) per point on streamlines and
        save it in hd5 file.

    Parameters
    ----------
    bundle : string
        Name of bundle being analyzed
    metric : matrix of float values
        dti metric e.g. FA, MD
    dt : DataFrame
        DataFrame to be populated
    pname : string
        Name of the dti metric
    ind : integer list
        ind tells which disk number a point belong.
    dir : string
        path of output directory

    """
    dt["streamline"] = []
    dt["disk"] = []
    dt[pname] = []

    values = map_coordinates(metric, bundle._data.T,
                             order=1)

    dt["disk"].extend(ind[list(range(len(values)))]+1)
    dt[pname].extend(values)

    for st_i in range(len(bundle)):

        st = bundle[st_i]
        dt["streamline"].extend([st_i]*len(st))

    file_name = pname

    save_buan_profiles_csv(os.path.join(dir, file_name), dt)


def buan_bundle_profiles(mb, bd, org_bd, measure,
                         no_disks=100, out_dir=''):
    """
    Applies statistical analysis on bundles and saves the results
    in a directory specified by ``out_dir``.


    References
    ----------
    .. [Chandio2020] Chandio, B.Q., Risacher, S.L., Pestilli, F., Bullock, D.,
    Yeh, FC., Koudoro, S., Rokem, A., Harezlak, J., and Garyfallidis, E.
    Bundle analytics, a computational framework for investigating the
    shapes and profiles of brain pathways across populations.
    Sci Rep 10, 17149 (2020)

    """

    t = time()


    mbundles = load_tractogram(mb, reference='same',
                               bbox_valid_check=False).streamlines
    bundles = load_tractogram(bd, reference='same',
                              bbox_valid_check=False).streamlines
    orig_bundles = load_tractogram(org_bd, reference='same',
                                   bbox_valid_check=False).streamlines

    if len(orig_bundles) > 5:

        indx = assignment_map(bundles, mbundles, no_disks)
        ind = np.array(indx)


        metric, affine = load_nifti(measure)

        affine_r = np.linalg.inv(affine)
        transformed_orig_bundles = transform_streamlines(orig_bundles,
                                                         affine_r)

        fm = measure[:-7]

        dt = dict()

        anatomical_measures(transformed_orig_bundles, metric, dt, fm,
                             ind, out_dir)


    print("total time taken in minutes = ", (-t + time())/60)


if __name__ == "__main__":
   
    # Create Brainlife's output dirs if don't exist
    if not os.path.exists('output'):
        os.mkdir('output')

    # Read Brainlife's config.json
    with open('config.json', encoding='utf-8') as config_json:
        config = json.load(config_json)


    model_bundle = config.get('model_bundle')
    rec_bundle = config.get('rec_bundle')
    org_bundle = config.get('org_bundle')
    no_disks = config.get('no_disks')
    measure = config.get('measure')


    out_dir = os.path.join(output', model_bundle[:-4])


    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    
    buan_bundle_profiles(model_bundle, rec_bundle , org_bundle, measure, int(no_disks),
                         out_dir)
