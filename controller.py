from var_dump import var_dump
from framework.generator import Generator
from framework.feature_collection import FeatureCollection
import sys
import os
import webbrowser

def generate_next(fcol, generator):
    feature_model = fcol.load_next()

    feature_model.parse_feature()

    for x in feature_model.get_scenarios_collection().get_scenario_models():
        lst = []
        lst.append(feature_model.get_scenarios_collection().get_background().get_background_final())
        lst.append(x.get_scenario_final())
        
        generator.load(lst, x.title)

def run():
    feature_files = []

    if '-all' in sys.argv and '-t' in sys.argv:
        print("ERROR: '-all' and '-t' cannot be used together.")
        return

    if '-all' in sys.argv and '-t' not in sys.argv:
        feature_files = os.listdir('features')
        feature_files = [ x for x in feature_files if ".feature" in x ]
        feature_files = ['features/' + s for s in feature_files]    

    if '-t' in sys.argv and '-all' not in sys.argv:
        if len(sys.argv) < sys.argv.index('-t') + 2:
            print('ERROR: Please specify the desired feature file after the \'-t\' parameter')
            return
        else:
            if '.feature' not in sys.argv[sys.argv.index('-t') + 1]:
               print('ERROR: Please specify the desired feature file after the \'-t\' parameter')
               return
            feature_files.append('features/' + sys.argv[sys.argv.index('-t') + 1])

    if '-all' not in sys.argv and '-t' not in sys.argv:
        print('ERROR: Please specify a feature file.')
        return
    generator = Generator()

    fcol = FeatureCollection(feature_files)

    for x in range(len(fcol.feature_files)):
        generate_next(fcol, generator)
    
    print("SUCCESS: Files were generated successfully. Please check inside the 'features/steps' folder to see the test cases.")

    if '-run' in sys.argv:
        os.chdir(os.getcwd()+"/tests")
        os.system("pytest --html=report.html")
        webbrowser.open_new_tab("report.html")

def help():
    print()
    print("This manual will explain all possible parameters.")
    print()
    print("Syntax: text2test [-t|all|run|h] [--help]")
    print("options:")
    print("h     Print this Help.")
    print("help  Print this Help.")
    print("t     Generate a test from a specific feature file.")
    print("all   Generate tests from all feature files inside features folder.")
    print("run   Execute generated test cases and generate a report.")
    print()

if __name__ == '__main__':
    if '-h' in sys.argv or '--help' in sys.argv:
        help()
    else:
        run()
    