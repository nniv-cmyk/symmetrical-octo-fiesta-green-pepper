import torch
import torch.nn as nn

class SpatialPyramidPooling(nn.Module):
    def __init__(self, pool_type='max', levels=[1, 2, 4]):
        # Call the super constructor
        super(SpatialPyramidPooling, self).__init__()
        
        # Save the type of pooling to be used ('max' or 'avg')
        self.pool_type = pool_type
        
        # Save the levels (e.g., [1, 2, 4])
        self.levels = levels
        
        # Choose the type of pooling to use
        self.pool = nn.AdaptiveAvgPool2d(1) if pool_type == 'avg' else nn.AdaptiveMaxPool2d(1)
    
    def forward(self, x):
        # Get the shape of the input tensor
        N, C, H, W = x.shape
        
        # Initialize a list to store the output
        out = []
        
        # Loop through each level
        for level in self.levels:
            # Calculate the height and width of each pooling region for this level
            h_pooled = int(H / level)
            w_pooled = int(W / level)
            
            # Loop through each region in the height direction
            for i in range(level):
                # Loop through each region in the width direction
                for j in range(level):
                    # Determine the start and end indices for this region in the height direction
                    h_start = i * h_pooled
                    h_end = (i + 1) * h_pooled
                    
                    # Determine the start and end indices for this region in the width direction
                    w_start = j * w_pooled
                    w_end = (j + 1) * w_pooled
                    
                    # Get the portion of the input tensor corresponding to this region
                    x_pooled = x[:, :, h_start:h_end, w_start:w_end]
                    
                    # Apply the pooling operation to this region
                    x_pooled = self.pool(x_pooled)
                    
                    # Add the result to the list of outputs
                    out.append(x_pooled)
        
        # Concatenate all the outputs along the channel dimension
        out = torch.cat(out, dim=1)
        
        # Return the final output
        return out
