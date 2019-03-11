def calcVolumes(heights_list, features, delta, cell_size):
    """Calculate the volume of each delta for each segment"""
    min_h = min(heights_list)
    volumes = []
    for feat in features: # iterate over the segments
        volume = []
        up_limit = min_h + delta
        tmp_len = 0
        num_of_cells = 0
        for h in heights_list: # This list is already sorted
            h_string = str(h)
            if h == int(h):  # The table represent 15.0 as 15
                h_string = str(int(h))
            num_of_cells += feat[h_string] # Calculate number of cells for populating the next delta 
            if h < up_limit:
                tmp_len += (up_limit - h)*feat[h_string] # This is the overall height
            else:
                volume.insert(0,tmp_len*cell_size) # finished with previous delta
                up_limit += delta  # setup the next delta
                while up_limit <= h : # if the next delta has no data in it, still add the volume of the one before
                    volume.insert(0,tmp_len*cell_size)
                    up_limit += delta
                tmp_len = (num_of_cells - feat[h_string])*delta # add the cells from the previous deltas
                tmp_len += (up_limit - h)*feat[h_string] # populate the current pixel value
        volume.insert(0,tmp_len*cell_size) # append the last volume clculations
        volumes.append({'SEGMENT' : int(feat['SEGMENT']), 'data' : volume}) # append to all features list
    return(volumes)