import sklearn.metrics as m
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

def plot_sigma_clusters(x_val, y_hat, y_val_upper_std,y_val_lower_std, y_in_std):

    plt.figure(figsize=(14, 6))
    plt.title('Sigma clusters in validation data | predictions')

    # plot data (with and without noise addition)

    plt.plot(x_val, y_hat, '*', color='grey')

    # plt.plot(x, y_1+ threshold, '*', color='darkgreen' ) # upper bound
    # plt.plot(x, y_1- threshold, '.', color='darkblue' ) # lower bound

    plt.plot(y_val_upper_std[0], y_val_upper_std[1], '.', color='green')
    plt.plot(y_val_lower_std[0], y_val_lower_std[1], '.', color='blue')
    plt.plot(y_in_std[0], y_in_std[1], '.', color='pink')

    plt.legend([r'y predictions', r'obs. values upper bound', r'obs. values lower bound',
                r'obs. values in bound'])
    plt.xlabel(r'$x$');
    plt.ylabel(r'$y$');

def plot_sigma_error_predictions(x_val, y_val, y_hat, sigma_real, sigma_hat):
    fig, ax1 = plt.subplots(figsize=(14, 6))

    ax1.plot(x_val, y_val, '.', color='purple')
    ax1.errorbar(x_val, y_hat, yerr=np.sqrt(sigma_real), color='red', fmt='.');
    ax1.errorbar(x_val, y_hat, yerr=sigma_hat.sqrt(), color='green', fmt='.');

    plt.title('Real sigma vs. Predicted sigma');
    plt.legend([r'Validation data', r'Real sigma', 'Predicted sigma'], loc='upper left');


def filter_extreme_values(x_val, y_val, y_pred, std_factor):
    """
    Extreme values are the ones that deviate more than 1sigma from predictions (predictions values with more error)
    :param y_val: validation dataset
    :param y_pred: predicted y_values
    :return:
    """
    y_std = np.array(y_val.size * [np.std(y_val)]) * std_factor  # get the std of real data. Use it as a threshold

    # init result arrays
    y_val_upper_std = [x_val, y_val]
    y_val_lower_std = [x_val, y_val]
    y_extr = [x_val, y_val]

    # filter values above or below threshold, y_pred +- std
    y_val_upper_std = np.ma.masked_equal(np.where(y_val_upper_std[1] > y_pred + y_std, y_val_upper_std, 0),0)
    y_val_lower_std = np.ma.masked_equal(np.where(y_val_lower_std[1] < y_pred - y_std, y_val_lower_std, 0),0)
    y_val_in_std = np.ma.masked_equal(np.where(np.logical_and((y_extr[1] > (y_pred - y_std)), (y_extr[1] < (y_pred + y_std))), y_extr, 0),0)

    return y_val_upper_std, y_val_lower_std, y_val_in_std, y_std

def extreme_model_performane(x_val, y_val, y_hat, sigma_hat, std_factor, display_plots):
    y_val_upper_std, y_val_lower_std, y_val_in_std, y_std = filter_extreme_values(x_val, y_val, y_hat, std_factor)  # use [:,[0]] to get rid of sigma component

    xy_hat = [x_val, y_hat]
    xy_sigma_hat = [x_val, sigma_hat]

    print('\nExtreme values performance:\n ')

    print('- Upper bound - ' + str(y_val_upper_std[0].count()) + ' Y pts  +sigma ' + str(round(std_factor, 2)) +  ': \n')
    y_hat_upper = np.where(xy_hat[0] in y_val_upper_std[0], xy_hat, 0)
    sigma_val_upper = (y_hat_upper - y_val_upper_std) ** 2  # get real sigma
    sigma_hat_upper = np.where(xy_sigma_hat[0] in y_val_upper_std[0], xy_hat, 0)

    print('R2 y_hat: {}'.format(m.r2_score(y_val_upper_std, y_hat_upper)))  # filter y_hat values in upper bound
    print('RMSE y_hat: {}'.format(m.mean_absolute_error(y_val_upper_std, y_hat_upper)))  # filter y_hat values in upper bound
    print('MAE sigma_hat : {}'.format(m.mean_absolute_error(np.sqrt(sigma_val_upper), np.sqrt(sigma_hat_upper))))

    print('-\n Lower bound - ' + str(y_val_lower_std[0].count()) + ' Y pts -sigma ' + str(round(std_factor, 2)) +  ': \n')
    y_hat_lower = np.where(xy_hat[0] in y_val_lower_std[0], xy_hat, 0)  # filter y_hat values in lower bound
    sigma_val_lower = (y_hat_upper - y_val_lower_std) ** 2  # get real sigma
    sigma_hat_lower = np.where(xy_sigma_hat[0] in y_val_lower_std[0], xy_hat, 0)

    print('R2 y_hat: {}'.format(m.r2_score(y_val_lower_std, y_hat_lower)))  # filter y_hat values in upper bound
    print('RMSE y_hat: {}'.format(m.mean_absolute_error(y_val_lower_std, y_hat_lower)))
    print('MAE sigma_hat: {}'.format(m.mean_absolute_error(np.sqrt(sigma_val_lower), np.sqrt(sigma_hat_lower))))

    print('-\n In bound - ' + str(y_val_in_std[0].count()) + ' Y pts in [+sigma ' + str(round(std_factor, 2)) +  ',' +  '-sigma ' + str(std_factor) + ']: \n')
    y_hat_in = np.where(xy_hat[0] in y_val_in_std[0], xy_hat, 0)
    sigma_val_in = (y_hat_in - y_val_in_std) ** 2  # get real sigma
    sigma_hat_in = np.where(xy_sigma_hat[0] in y_val_in_std[0], xy_hat, 0)

    print('R2 y_hat: {}'.format(m.r2_score(y_val_in_std, y_hat_in)))  # filter y_hat values in upper bound
    print('RMSE y_hat: {}'.format(m.mean_absolute_error(y_val_in_std, y_hat_in)))  # filter y_hat values in lower bound
    print('MAE sigma_hat: {}'.format(m.mean_absolute_error(np.sqrt(sigma_val_in), np.sqrt(sigma_hat_in))))

    if display_plots:
        plot_sigma_clusters(x_val, y_hat, y_val_upper_std, y_val_lower_std, y_val_in_std)


def overall_model_performance(x_val, y_val, y_hat_t, sigma_hat, std_factor=1, extreme_values_performance=False, display_plots=False):
    """
    Measure the overall performance of both predictions: y and sigma
    :param x_val: x validation dataset
    :param y_val: validation dataset
    :param y_pred: predicted y values
    :param sigma_pred: predicted sigma values
    :return:
    """
    y_hat = y_hat_t.numpy() if type(y_hat_t) is not np.ndarray else y_hat_t

    sigma_val = (y_hat - y_val)**2 # get real sigma

    aux_sigma_val = np.array(sigma_val.size * [np.mean(sigma_val)])

    print('Global model performance: \n')
    print('- R2 y_hat: {} '.format(m.r2_score(y_val, y_hat))) # proportion of variation in y_val explained by the y_pred --> this is proportionally inverse to sigma_pred
    print('- RMSE y_hat: {} '.format(m.mean_squared_error(y_val, y_hat)))
    print('- RMSE sigma_hat: {} '.format(m.mean_squared_error(np.sqrt(abs(sigma_val)), np.sqrt(abs(sigma_hat)))))

    if display_plots:
        plot_sigma_error_predictions(x_val, y_val, y_hat, sigma_val, sigma_hat)

    if extreme_values_performance:
       extreme_model_performane(x_val, y_val, y_hat, sigma_hat, std_factor, display_plots)


def tests_prior_beliefs(x_val, y_val, y_hat_t, sigma_hat_t):
    '''

    :return:
    '''
    y_hat = y_hat_t.numpy() if type(y_hat_t) is not np.ndarray else y_hat_t
    sigma_hat = sigma_hat_t.numpy() if type(sigma_hat_t) is not np.ndarray else sigma_hat_t
    sigma_val = (y_hat - y_val) ** 2  # get real sigma

    print("--------------------------------- Distribution Tests --------------------------------------------")
    print('\x1b[0m' + "\n ----> H0: Test Normal Distribution \n - Test de Shapiro-Wilks")
    _feat_test = {'x_val':x_val, 'y_val':y_val, 'y_hat':y_hat, 'sigma_real': sigma_val, 'sigma_hat': sigma_hat}
    for name, feature in _feat_test.items():
        p_value = stats.shapiro(feature)[1]
        is_passed = "\x1b[6;30;42m" + "Aceptance" if p_value > 0.05 else "\x1b[6;30;41m" + 'Negation'
        print(is_passed + " - p_value = " + str(round(p_value,10)) +  " Normal distribution: - "  + str(name))

    print('\x1b[0m' + "\n ----> H0: The two (sigma_hat and sigma_real) distributions are identical \n- Test de Kolmogorov-Smirnov")
    p_value = stats.ks_2samp(sigma_hat, sigma_val)[1]
    is_passed = "\x1b[6;30;42m" + "Aceptance"  if p_value > 0.05 else "\x1b[6;30;41m" + 'Negation'
    print(is_passed + " - p_value = " + str(round(p_value,10)) +  " equivalence of distributions - sigma_hat - sigma_val")

    print('\x1b[0m' + "\n ----> H0: The y_hat | sigma_hat keeps its source distirbution \n" + "- Test de Chi-Square")
    p_value = stats.chisquare(y_hat, y_val)[1]
    is_passed = "\x1b[6;30;42m" + "Aceptance" if p_value > 0.05 else "\x1b[6;30;41m" + 'Negation'
    print(is_passed + " - p_value = " + str(round(p_value,10)) +  " keeps its source distirbution: y_val - y_hat")

    p_value = stats.chisquare(sigma_hat, sigma_val)[1]
    is_passed = "\x1b[6;30;42m" + "Aceptance" if p_value > 0.05 else "\x1b[6;30;41m" + 'Negation'
    print(is_passed + " - p_value = " + str(round(p_value,10)) + " keeps its source distirbution: sigma_val - sigma_hat")

    print('\x1b[0m' + "\n--------------------------------- Homoscedasticity Tests --------------------------------------------")
    print("Build the sigma clusters in y validation")

    y_val_upper_std, y_val_lower_std, y_val_in_std, y_std = filter_extreme_values(x_val, y_val, y_hat, std_factor=1/4)

    print('\n----> H0: The sigma clusters of validation data have homogenenous variance')
    print("- Test de Levene")
    p_value = stats.levene(y_val_upper_std[0].data, y_val_in_std[0].data)[1]
    is_passed = "\x1b[6;30;42m" + "Aceptance" if p_value > 0.05 else "\x1b[6;30;41m" + 'Negation'
    print(is_passed + " - p_value = " + str(round(p_value,10)) + " sigma clusters of validation data have homogenenous variance: upper sigma - inside sigma threshold")

    p_value = stats.levene(y_val_upper_std[0].data, y_val_lower_std[0].data)[1]
    is_passed = "\x1b[6;30;42m" + "Aceptance" if p_value > 0.05 else "\x1b[6;30;41m" + 'Negation'
    print(is_passed + " - p_value = " + str(round(p_value,10)) + " sigma clusters of validation data have homogenenous variance: upper sigma - lower sigma threshold")

    p_value = stats.levene(y_val_lower_std[0].data, y_val_in_std[0].data)[1]
    is_passed = "\x1b[6;30;42m" + "Aceptance" if p_value > 0.05 else "\x1b[6;30;41m" + 'Negation'
    print(is_passed + " - p_value = " + str(round(p_value,10)) + " sigma clusters of validation data have homogenenous variance: lower sigma - inside sigma threshold")


    print('\x1b[0m' + "\n--------------------------------- Plot distributions and sigma clusters--------------------------------------------")
    print("---- Plot distributions for each variable \n")
    for name, feature in _feat_test.items():
        plt.figure(); sns.kdeplot(feature, shade=True).set_title(str(name));  plt.figure(); plt.title(str(name)); stats.probplot(feature, dist='norm', fit=True, rvalue=True, plot=plt);

    plot_sigma_clusters(x_val, y_hat, y_val_upper_std, y_val_lower_std, y_val_in_std)