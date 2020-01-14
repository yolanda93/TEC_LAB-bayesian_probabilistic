import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Activation, Concatenate
from tensorflow.keras.callbacks import EarlyStopping, TensorBoard, ReduceLROnPlateau
import tensorflow.keras as K
from tensorflow_probability import distributions as tfd

class MDN(tf.keras.Model):

    def __init__(self, neurons=100, components=2, no_parameters=3):
        super(MDN, self).__init__(name="MDN")
        self.neurons = neurons
        self.components = components
        self.no_parameters = no_parameters

        self.h1 = Dense(neurons, activation="relu", name="h1")
        self.h2 = Dense(neurons, activation="relu", name="h2")

        self.alphas = Dense(components, activation="softmax", name="alphas")
        self.mus = Dense(components, name="mus")
        self.sigmas = Dense(components, activation="nnelu", name="sigmas")
        self.pvec = Concatenate(name="pvec")

    def call(self, inputs):
        x = self.h1(inputs)
        x = self.h2(x)

        alpha_v = self.alphas(x)
        mu_v = self.mus(x)
        sigma_v = self.sigmas(x)

        return self.pvec([alpha_v, mu_v, sigma_v])

    def nnelu(input):
        """ Computes the Non-Negative Exponential Linear Unit
        """
        return tf.add(tf.constant(1, dtype=tf.float32), tf.nn.elu(input))


    def slice_parameter_vectors(self, parameter_vector):
        """ Returns an unpacked list of paramter vectors.
        """
        return [parameter_vector[:, i * self.components:(i + 1) * self.components] for i in range(self.no_parameters)]


    def gnll_loss(self, y, parameter_vector):
        """ Computes the mean negative log-likelihood loss of y given the mixture parameters.
        """
        alpha, mu, sigma = self.slice_parameter_vectors(parameter_vector)  # Unpack parameter vectors

        gm = tfd.MixtureSameFamily(
            mixture_distribution=tfd.Categorical(probs=alpha),
            components_distribution=tfd.Normal(
                loc=mu,
                scale=sigma))

        log_likelihood = gm.log_prob(tf.transpose(y))  # Evaluate log-probability of y

        return -tf.reduce_mean(log_likelihood, axis=-1)


    tf.keras.utils.get_custom_objects().update({'nnelu': Activation(nnelu)})


class DNN(tf.keras.Model):
    def __init__(self, neurons=100):
        super(DNN, self).__init__(name="DNN")
        self.neurons = neurons

        self.h1 = Dense(neurons, activation="relu", name="h1")
        self.h2 = Dense(neurons, activation="relu", name="h2")
        self.out = Dense(1, activation="linear", name="out")

    def call(self, inputs):
        x = self.h1(inputs)
        x = self.h2(x)
        return self.out(x)



