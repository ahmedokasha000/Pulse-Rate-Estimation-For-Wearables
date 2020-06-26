def AgeAndRHR(metadata, filename):

    # Load the heart rate timeseries
    hr_data = np.load(filename)['hr']
    # Compute the resting heart rate from the timeseries by finding the
    # lowest 5th percentile value in hr_data
    rhr = np.percentile(hr_data, 5)

    # Find the subject ID from the filename.
    subject = filename.split('/')[-1][:-4]

    # Find the age group for this subject in metadata.
    filtt = metadata["subject"] == subject
    age_group = (metadata[filtt]).age.values[0]
    # Find the sex for this subject in metadata.
    sex = (metadata[filtt]).sex.values[0]

    return age_group, sex, rhr


df = pd.DataFrame(data=[AgeAndRHR(metadata, filename) for filename in hr_filenames],
                  columns=['age_group', 'sex', 'rhr'])
