import numpy as np
# import pandas as pd
import argparse
# import matplotlib.pyplot as plt
import mne.io




def main():
    parser = argparse.ArgumentParser(description='Multilayer Perceptron')
    parser.add_argument('--dataset', type=str, default='/home/fli/sgoinfre/files', help='Path to data')
    parser.add_argument('--mode', type=str, default='train', choices=['train', 'predict'],
                        help='Mode: train or predict')

    args = parser.parse_args()

    raw = mne.io.read_raw_edf(args.dataset + '/S001/S001R09.edf')

    print("Plotting raw data before filtering...")
    before = raw.plot(block=True, duration=15.0, title='Before Filtering')

    raw.load_data()
    raw.filter(l_freq=12.0, h_freq=50.0)
    raw.notch_filter(freqs=[50])

    print("Plotting data after filtering...")
    after = raw.plot(block=True, duration=15.0, title='After Filtering')

    before.savefig('eeg_before_filtering.png', dpi=300, bbox_inches='tight')
    after.savefig('eeg_after_filtering.png', dpi=300, bbox_inches='tight')



if __name__ == "__main__":
    main()