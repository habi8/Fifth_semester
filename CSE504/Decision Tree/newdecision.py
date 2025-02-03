import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, recall_score

def specificity_score(y_true, y_pred, average='weighted'):
    ''' Function to calculate specificity score '''
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_true, y_pred)
    tn = cm[0][0]
    fp = cm[0][1]
    specificity = tn / (tn + fp)
    return specificity

# Load the dataset
col_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
data = pd.read_csv("IRIS.csv", skiprows=1, header=None, names=col_names)

# Define the Node class
class Node():
    def __init__(self, feature_index=None, threshold=None, left=None, right=None, info_gain=None, value=None):
        ''' constructor ''' 
        
        # for decision node
        self.feature_index = feature_index
        self.threshold = threshold
        self.left = left
        self.right = right
        self.info_gain = info_gain
        
        # for leaf node
        self.value = value

# Define the DecisionTreeClassifier class
class DecisionTreeClassifier():
    def __init__(self, min_samples_split=2, max_depth=2):
        ''' constructor '''
        
        # initialize the root of the tree 
        self.root = None
        
        # stopping conditions
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        
    def build_tree(self, dataset, curr_depth=0):
        ''' recursive function to build the tree ''' 
        
        X, Y = dataset[:,:-1], dataset[:,-1]
        num_samples, num_features = np.shape(X)
        
        # split until stopping conditions are met
        if num_samples >= self.min_samples_split and curr_depth <= self.max_depth:
            # find the best split
            best_split = self.get_best_split(dataset, num_samples, num_features)
            # check if information gain is positive
            if best_split["info_gain"] > 0:
                # recur left
                left_subtree = self.build_tree(best_split["dataset_left"], curr_depth + 1)
                # recur right
                right_subtree = self.build_tree(best_split["dataset_right"], curr_depth + 1)
                # return decision node
                return Node(best_split["feature_index"], best_split["threshold"], 
                            left_subtree, right_subtree, best_split["info_gain"])
        
        # compute leaf node
        leaf_value = self.calculate_leaf_value(Y)
        # return leaf node
        return Node(value=leaf_value)
    
    def get_best_split(self, dataset, num_samples, num_features):
        ''' function to find the best split '''
        
        # dictionary to store the best split
        best_split = {}
        max_info_gain = -float("inf")
        
        # loop over all the features
        for feature_index in range(num_features):
            feature_values = dataset[:, feature_index]
            possible_thresholds = np.unique(feature_values)
            # loop over all the feature values present in the data
            for threshold in possible_thresholds:
                # get current split
                dataset_left, dataset_right = self.split(dataset, feature_index, threshold)
                # check if childs are not null
                if len(dataset_left) > 0 and len(dataset_right) > 0:
                    y, left_y, right_y = dataset[:, -1], dataset_left[:, -1], dataset_right[:, -1]
                    # compute information gain
                    curr_info_gain = self.information_gain(y, left_y, right_y, "gini")
                    # update the best split if needed
                    if curr_info_gain > max_info_gain:
                        best_split["feature_index"] = feature_index
                        best_split["threshold"] = threshold
                        best_split["dataset_left"] = dataset_left
                        best_split["dataset_right"] = dataset_right
                        best_split["info_gain"] = curr_info_gain
                        max_info_gain = curr_info_gain
                        
        # return best split
        return best_split
    
    def split(self, dataset, feature_index, threshold):
        ''' function to split the data '''
        
        dataset_left = np.array([row for row in dataset if row[feature_index] <= threshold])
        dataset_right = np.array([row for row in dataset if row[feature_index] > threshold])
        return dataset_left, dataset_right
    
    def information_gain(self, parent, l_child, r_child, mode="entropy"):
        ''' function to compute information gain '''
        
        weight_l = len(l_child) / len(parent)
        weight_r = len(r_child) / len(parent)
        if mode == "gini":
            gain = self.gini_index(parent) - (weight_l * self.gini_index(l_child) + weight_r * self.gini_index(r_child))
        elif mode == "chi_square":
            gain = self.chi_square(parent, l_child, r_child)
        else:
            gain = self.entropy(parent) - (weight_l * self.entropy(l_child) + weight_r * self.entropy(r_child))
        return gain

    def entropy(self, y):
        ''' function to compute entropy '''
        
        class_labels = np.unique(y)
        entropy = 0
        for cls in class_labels:
            p_cls = len(y[y == cls]) / len(y)
            entropy += -p_cls * np.log2(p_cls)
        return entropy
    
    def gini_index(self, y):
        ''' function to compute gini index '''
        
        class_labels = np.unique(y)
        gini = 0
        for cls in class_labels:
            p_cls = len(y[y == cls]) / len(y)
            gini += p_cls ** 2
        return 1 - gini

    def chi_square(self, parent, l_child, r_child):
        ''' function to compute chi-square '''
        parent_classes, parent_counts = np.unique(parent, return_counts=True)
        chi_square_value = 0

        for cls in parent_classes:
            parent_count = parent_counts[np.where(parent_classes == cls)][0]
            expected_l = len(l_child) * (parent_count / len(parent))
            expected_r = len(r_child) * (parent_count / len(parent))

            actual_l = len(l_child[l_child == cls])
            actual_r = len(r_child[r_child == cls])

            if expected_l > 0:
                chi_square_value += ((actual_l - expected_l) ** 2) / expected_l
            if expected_r > 0:
                chi_square_value += ((actual_r - expected_r) ** 2) / expected_r

        return chi_square_value

    def calculate_leaf_value(self, Y):
        ''' function to compute leaf node '''
        
        Y = list(Y)
        return max(Y, key=Y.count)
    
    def print_tree(self, tree=None, indent=" "):
        ''' function to print the tree '''
        
        if not tree:
            tree = self.root

        if tree.value is not None:
            print(tree.value)

        else:
            print("X_" + str(tree.feature_index), "<=", tree.threshold, "?", tree.info_gain)
            print("%sleft:" % (indent), end="")
            self.print_tree(tree.left, indent + indent)
            print("%sright:" % (indent), end="")
            self.print_tree(tree.right, indent + indent)
    
    def fit(self, X, Y):
        ''' function to train the tree '''
        
        if Y.ndim == 1:
            Y = Y.reshape(-1, 1)
        dataset = np.concatenate((X, Y), axis=1)
        self.root = self.build_tree(dataset)
    
    def predict(self, X):
        ''' function to predict new dataset '''
        
        predictions = [self.make_prediction(x, self.root) for x in X]
        return predictions

    def make_prediction(self, x, tree):
        ''' function to predict a single data point '''
        
        if tree.value != None:
            return tree.value
        feature_val = x[tree.feature_index]
        if feature_val <= tree.threshold:
            return self.make_prediction(x, tree.left)
        else:
            return self.make_prediction(x, tree.right)

# Prepare the data
X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values

# Perform K-Fold Cross Validation
def k_fold_cross_validation(model, X, y, k=5):
    n_samples = len(X)
    fold_size = n_samples // k

    indices = np.arange(n_samples)
    np.random.shuffle(indices)

    accuracy_scores = []
    f1_scores = []
    d2h_scores = []

    for i in range(k):
        val_indices = indices[i * fold_size:(i + 1) * fold_size]
        train_indices = np.concatenate((indices[:i * fold_size], indices[(i + 1) * fold_size:]))

        X_train, X_val = X[train_indices], X[val_indices]
        y_train, y_val = y[train_indices], y[val_indices]

        model.fit(X_train, y_train)
        y_pred = model.predict(X_val)
        
        accuracy = accuracy_score(y_val, y_pred)
        f1 = f1_score(y_val, y_pred, average='weighted')

        # Calculate Distance to Heaven (D2H)
        sensitivity = recall_score(y_val, y_pred, average='weighted')
        specificity = specificity_score(y_val, y_pred, average='weighted')
        d2h = np.sqrt((1 - sensitivity) ** 2 + (1 - specificity) ** 2)
        
        accuracy_scores.append(accuracy)
        f1_scores.append(f1)
        d2h_scores.append(d2h)
    
    return np.mean(accuracy_scores), np.mean(f1_scores), np.mean(d2h_scores)

classifier = DecisionTreeClassifier(min_samples_split=3, max_depth=3)

# Perform 5-fold cross-validation
average_accuracy, average_f1_score,d2h_score = k_fold_cross_validation(classifier, X, Y.flatten(), k=5)

print(f"Average Accuracy across 5 folds: {average_accuracy:.4f}")
print(f"Average F1 Score across 5 folds: {average_f1_score:.4f}")
print(f"Average d2h Score across 5 folds: {d2h_score:.4f}")
