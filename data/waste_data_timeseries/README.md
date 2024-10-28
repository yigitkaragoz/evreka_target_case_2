# Dataset Definition

- **Service Points:** Bin locations, a service point may contain more than one bin.  
- **Visit:** Waste collection truck visits a service point.  
- **SPID:** Service Point ID  
    Each record in the dataset is recorded at a visit when bins are emptied to the truck.
    - Assume that all bins have the same size.
    - You can ignore some service points if you don’t think there is enough data for that location. Please explain which ones you have ignored and why.
- **# Waste:** number of bins emptied in that visit for that waste type.
- **% Waste:** avg. fullness percentage of the bins emptied.

**Example:** #Paper: 2, %50 means that 2 bins emptied with an avg. fullness of 50%. 
It could be 2 bins at 50% or one with 90% and the other with 10%. 
If you see any data bigger than 100%, that means the bin is full and overflowed.
