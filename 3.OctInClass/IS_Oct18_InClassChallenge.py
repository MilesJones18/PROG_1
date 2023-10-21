



def myDictionary(request):
    vehicles = {'Ford':['Mustang','F-150','GT40',
                        'Bronco'],
                'Chevy':['Silverado', 'Corvette','Equinox'
                         'Cruise'],
                'Toyota':['Camry','Corolla','Supra',
                          'Tundra']}
    
    for brand, model in vehicles.items():
        if request in model:
            return brand
        



def menu():
    search = input("What model are you looking for? ")
    result = myDictionary(search)
    print(result)



if __name__ == '__main__':
    menu()