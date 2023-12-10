class Mapping:
    def __init__(self, tag, file):
        self.tag = tag
        self.file = file
        self.map = []
        for i in enumerate(self.file):
            if len(i[1]) == 0 and len(self.map) > 0:
                break
            if i[1] == self.tag or len(self.map) > 0:
                try:
                    if len(self.file[i[0]+1]) != 0: self.map.append(self.file[i[0]+1])
                except:
                    continue
        self.dest_r = []
        self.src_r = []
        self.rng_len =[]
        for i in self.map:
            self.split = i.split(' ')
            self.dest_r.append(int(self.split[0]))
            self.src_r.append(int(self.split[1]))
            self.rng_len.append(int(self.split[2]))

    def m(self, src):
        for i in enumerate(self.src_r):
            if src >= i[1] and src <= i[1]+(self.rng_len[i[0]]-1):
                return self.dest_r[i[0]] + (src - i[1])
        return src
        
            
file = open("input.txt", 'r').read().split('\n')
seed = Mapping("seed-to-soil map:", file)
soil = Mapping("soil-to-fertilizer map:", file)
fertilizer = Mapping("fertilizer-to-water map:", file)
water = Mapping("water-to-light map:", file)
light = Mapping("light-to-temperature map:", file)
temperature = Mapping("temperature-to-humidity map:", file)
humidity = Mapping("humidity-to-location map:", file)

seeds = file[0].split(' ')[1:]
locations = []
for i in seeds:
    locations.append(humidity.m(temperature.m(light.m(water.m(fertilizer.m(soil.m(seed.m(int(i)))))))))
print(min(locations))
        
        
