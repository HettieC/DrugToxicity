class Cache:
    localCache = set()

    def add(self, smiles: str) -> None:
        self.localCache.add(smiles)
    
    def is_cached(self, smiles: str) -> bool:
        return smiles in self.localCache
        

