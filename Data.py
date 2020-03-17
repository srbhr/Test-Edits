class Data:
    
    
    def __init__(self, path='Data/new 1.json'):
        self.data_path = path 
    
    def get_data(self, engine='Apertium'):
        
        try:
            import pandas as pd
            files = pd.read_json(self.data_path)
        except ImportError:
            print("Module Not Available")
        
        final = []
        
        n = len(files['id'])
        
        for _ in range(0, n-1):
            if str(files['mt'][_]) != 'None' and files['mt'][_]['engine'] == engine:
                source_ = files['source'][_]['content']
                mt_ = files['mt'][_]['content']
                target_ = files['target'][_]['content']
                
                if _is_inconsistent(source_, mt_, target_) == False:
                    final.append([source_, mt_, target_])
                
        if len(final) == 0:
            print('List is Empty, there is no Translation for that Particular engine')
        
        return final
    
    """
        This is just a method to check for inconsistency in Post-Edits, as someone has done some mischievious
        things while translating(Post-editing), Sentences have been repeated upto 4 times, words with long unwanted words 
        characters e.g. "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "adf&*^%&", etc. which are not there in the original 
        text.
    
    """
    def _is_inconsistent(self, a, b, c):
        a = a.split()
        b = b.split()
        c = c.split()
        if len(a) in range(0, len(c)+15) and len(a) in range(0, len(b)+15):
            for i, j in zip(b, c):
                if len(i) in range(0,20) and len(j) in range(0, 20):
                    return True
        else: 
            return False  
        