"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the
software.

Patients' data is held in an inflammation table (2D array) where each row
contains inflammation data for a single patient taken over a number of days
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.

    :param: data - A 2D array containing inflammation data,
                containing measurements for a single patient on
                all days

    :returns: An array of the mean values of the measurement for
                each day
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array.

    :param: data - A 2D array containing inflammation data,
                containing measurements for a single patient on
                all days

    :returns: An array of the maximum values of the measurement for
                each day
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2d inflammation data array.

    :param: data - A 2D array containing inflammation data,
                containing measurements for a single patient on
                all days

    :returns: An array of the minimum values of the measurement for
                each day
    """
    return np.min(data, axis=0)


def patient_normalise(data):
    """
    Normalise patient data from a 2D inflammation data array.

    NaN values are ignored, and normalised to 0.

    Negative values are rounded to 0.
    """
    if np.any(data < 0):
        raise ValueError('Inflammation values should not be negative')

    maxima = np.nanmax(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / maxima[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    normalised[normalised < 0] = 0
    return normalised


# TODO(lesson-design) Add Patient class
class Observation:
    def __init__(self, day, value):
        self.day = day
        self.value = value

    def __str__(self):
        return str(self.value)


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Patient(Person):
    """A patient in an inflammation study."""

    def __init__(self, name, observations=None):
        super().__init__(name)

        self.observations = []
        ### MODIFIED START ###
        if observations is not None:
            self.observations = observations
        ### MODIFIED END ###

    def add_observation(self, value, day=None):
        if day is None:
            try:
                day = self.observations[-1]['day'] + 1

            except IndexError:
                day = 0

        new_observation = Observation(day, value)

        self.observations.append(new_observation)
        return new_observation

    def __str__(self):
        return self.name

    @property
    def last_observation(self):
        return self.observations[-1]


# TODO(lesson-design) Implement data persistence
# TODO(lesson-design) Add Doctor class
class Doctor(Person):
    """A doctor in an inflammation study"""
    def __init__(self, name):
        super().__init__(name)
        self.observations = []
        self.list_of_patients = []

    def add_patient(self, patient=Patient):
        if patient is not Patient:
            raise TypeError("patient is not of Class PAtient")

        new_patient = Patient

        self.list.append(new_patient)
        return new_patient
