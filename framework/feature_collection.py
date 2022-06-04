from framework.feature_model import FeatureModel

#######################################
# FEATURE COLLECTION
#######################################

class FeatureCollection:

    def __init__(self, feature_files):
        self.feature_files = feature_files
        self.current_file_index = 0

    def load_next(self):
        if self.current_file_index >= len(self.feature_files):
            return None

        aux = FeatureModel(self.feature_files[self.current_file_index])

        self.current_file_index += 1
        
        return aux

    def __repr__(self):
        return self.feature_files[0] + "; " +self.feature_files[1]
        