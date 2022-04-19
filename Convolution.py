import numpy as np
def Conv(img, filter):
    m_channels, m_rows, m_cols = img.shape
    n_rows, n_cols = filter.shape
    r = np.zeros((m_rows-n_rows+1,m_cols-n_cols+1))
    #print(m_rows, m_cols, m_channels)

    for i in range(m_rows-n_rows+1):
        for j in range(m_cols-n_cols+1):
            for k in range(m_channels):
                r[i,j] += np.sum(np.multiply(img[k,i:n_rows+i,j:n_cols+j], filter))

    return r