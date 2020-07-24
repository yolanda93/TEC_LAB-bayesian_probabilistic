import numpy as np

def umal_regre_heterogeneous(size=1000, selected_zones=['Asymmetric', 'Symmetric', 'Uniform', 'Multimodal'],
                             split_train_test=True):
    lst = []
    points = np.random.beta(0.5, 1, 8 * size // 10) * 5 + 0.5
    zones = []

    if 'Asymmetric' in selected_zones:
        np.random.shuffle(points)
        lst += points.tolist()
        zones += [[len(lst), 'Asymmetric']]

    if 'Symmetric' in selected_zones:
        points = 3 * np.cos(np.linspace(0, 5, num=size)) - 2
        points = points + np.random.normal(scale=np.abs(points) / 4, size=size)
        lst += points.tolist()
        zones += [[len(lst), 'Symmetric']]

    if 'Uniform' in selected_zones:
        lst += [np.random.uniform(low=i, high=j)
                for i, j in zip(np.linspace(-2, -4.5, num=size // 2),
                                np.linspace(-0.5, 9., num=size // 2))]
        zones += [[len(lst), 'Uniform']]

    if 'Multimodal' in selected_zones:
        points = np.r_[8 + np.random.uniform(size=size // 2) * 0.5,
                       1 + np.random.uniform(size=size // 2) * 3.,
                       -4.5 + np.random.uniform(size=-(-size // 2)) * 1.5]

        np.random.shuffle(points)

        lst += points.tolist()
        zones += [[len(lst), 'Multimodal']]

    y_train_synthetic = np.array(lst).reshape(-1, 1)
    x_train_synthetic = np.arange(y_train_synthetic.shape[0]).reshape(-1, 1)
    x_train_synthetic = x_train_synthetic / x_train_synthetic.max()

    disord = np.arange(y_train_synthetic.shape[0])
    np.random.shuffle(disord)
    x_train_synthetic, y_train_synthetic = x_train_synthetic[disord], y_train_synthetic[disord]

    if split_train_test:
        # Train = 45%, Validation = 5%, Test = 50%
        x_test_synthetic = x_train_synthetic[:x_train_synthetic.shape[0] // 2]
        y_test_synthetic = y_train_synthetic[:x_train_synthetic.shape[0] // 2]
        y_train_synthetic = y_train_synthetic[x_train_synthetic.shape[0] // 2:]
        x_train_synthetic = x_train_synthetic[x_train_synthetic.shape[0] // 2:]

        x_valid_synthetic = x_train_synthetic[:x_train_synthetic.shape[0] // 10]
        y_valid_synthetic = y_train_synthetic[:x_train_synthetic.shape[0] // 10]
        y_train_synthetic = y_train_synthetic[x_train_synthetic.shape[0] // 10:]
        x_train_synthetic = x_train_synthetic[x_train_synthetic.shape[0] // 10:]

        return x_test_synthetic, y_test_synthetic, x_valid_synthetic, y_valid_synthetic, x_train_synthetic, y_train_synthetic, zones, lst

    return x_train_synthetic[disord], y_train_synthetic[disord], zones