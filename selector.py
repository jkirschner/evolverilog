"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

Note: Code unnecessary for our purposes was removed from the original file.

Some code was adjusted by Jared Kirschner
"""

import matplotlib
import matplotlib.pyplot as pyplot
import random
import bisect
import math
from copy import deepcopy

class OrganismPmf:
    """Represents a probability mass function.
    
    Values can be any hashable type; probabilities are floating-point.
    OrganismPmfs are not necessarily normalized.
    """

    def __init__(self, d=None, name=''):
        # if d is provided, use it; otherwise make a new dict
        if d == None:
            d = {}
        self.d = d
        self.name = name
        self.scalingFactor = 0

    def Copy(self):
        
        return OrganismPmf( 
                d=dict((org,fit) for org,fit in self.d.iteritems()) 
            )

    def Values(self):
        """Gets an unsorted sequence of values.

        Note: one source of confusion is that the keys in this
        dictionaries are the values of the OrganismHist/OrganismPmf, and the
        values are frequencies/probabilities.
        """
        return self.d.keys()

    def Items(self):
        """Gets an unsorted sequence of (value, freq/prob) pairs."""
        return self.d.items()

    def Print(self):
        """Prints the values and freqs/probs in ascending order."""
        for val, prob in sorted(self.d.iteritems()):
            print val, prob

    def Remove(self, x):
        """Removes a value.

        Throws an exception if the value is not there.

        Args:
            x: value to remove
        """
        del self.d[x]

    def Total(self):
        """Returns the total of the frequencies/probabilities in the map."""
        total = sum(self.d.values())
        return total

    def Prob(self, x):
        """Gets the probability associated with the value x.

        Args:
            x: number value

        Returns:
            float probability
        """
        return self.d.get(x, 0)
    
    def AddOrganism(self, organism):
        """Set the freq/prob associated with the value x.

        Args:
            x: number value
        """
        self.d[organism] = organism.getFitness()

    def Probs(self):
        """Gets an unsorted sequence of probabilities."""
        return self.d.values()

    def Normalize(self, fraction=1.0):
        """Normalizes this OrganismPmf so the sum of all probs is 1.

        Args:
            fraction: what the total should be after normalization
        """
        total = self.Total()
        if total == 0.0:
            raise ValueError('total probability is zero.')
            return
        
        self.scalingFactor = total
        
        factor = float(fraction) / total
        for x in self.d:
            self.d[x] *= factor
    
    def Random(self):
        """Chooses a random element from this OrganismPmf.

        Returns:
            float mean
        """
        target = random.random()
        total = 0.0
        for x, p in self.d.iteritems():
            total += p
            if total >= target:
                return x
        return x

    def Mean(self):
        """Computes the mean of a OrganismPmf.

        Returns:
            float mean
        """
        mu = 0.0
        for x, p in self.d.iteritems():
            mu += p * x
        return mu

    def Var(self, mu=None):
        """Computes the variance of a OrganismPmf.

        Args:
            mu: the point around which the variance is computed;
                if omitted, computes the mean

        Returns:
            float variance
        """
        if mu is None:
            mu = self.Mean()
            
        var = 0.0
        for x, p in self.d.iteritems():
            var += p * (x - mu)**2
        return var
        
    def Render(self):
        """Generates a sequence of points suitable for plotting.

        Returns:
            tuple of (sorted value sequence, freq/prob sequence)
        """
        
        d = {}
        for organism, fitness in self.Items():
            fn = fitness*self.scalingFactor
            d[fn] = d.get(fn,0) + 1
        
        return zip(*sorted(d.items()))

class Cdf(object):
    """Represents a cumulative distribution function.

    Attributes:
        xs: sequence of values
        ps: sequence of probabilities
        name: string used as a graph label.
    """
    def __init__(self, xs=None, ps=None, name=''):
        self.xs = xs or []
        self.ps = ps or []
        self.name = name

    def Values(self):
        """Returns a sorted list of values.
        """
        return self.xs

    def Items(self):
        """Returns a sorted sequence of (value, probability) pairs.

        Note: in Python3, returns an iterator.
        """
        return zip(self.xs, self.ps)

    def Append(self, x, p):
        """Add an (x, p) pair to the end of this CDF.

        Note: this us normally used to build a CDF from scratch, not
        to modify existing CDFs.  It is up to the caller to make sure
        that the result is a legal CDF.
        """
        self.xs.append(x)
        self.ps.append(p)

    def Prob(self, x):
        """Returns CDF(x), the probability that corresponds to value x.

        Args:
            x: number

        Returns:
            float probability
        """
        if x < self.xs[0]: return 0.0
        index = bisect.bisect(self.xs, x)
        p = self.ps[index-1]
        return p

    def Value(self, p):
        """Returns InverseCDF(p), the value that corresponds to probability p.

        Args:
            p: number in the range [0, 1]

        Returns:
            number value
        """
        if p < 0 or p > 1:
            raise ValueError('Probability p must be in range [0, 1]')

        if p == 0: return self.xs[0]
        if p == 1: return self.xs[-1]
        index = bisect.bisect(self.ps, p)
        if p == self.ps[index-1]:
            return self.xs[index-1]
        else:
            return self.xs[index]

    def Percentile(self, p):
        """Returns the value that corresponds to percentile p.

        Args:
            p: number in the range [0, 100]

        Returns:
            number value
        """
        return self.Value(p / 100.0)

    def Random(self):
        """Chooses a random value from this distribution."""
        return self.Value(random.random())
    
    def Sample(self, n):
        """Generates a random sample from this distribution.
        
        Args:
            n: int length of the sample
        """
        return [self.Random() for i in range(n)]

    def Mean(self):
        """Computes the mean of a CDF.

        Returns:
            float mean
        """
        old_p = 0
        total = 0.0
        for x, new_p in zip(self.xs, self.ps):
            p = new_p - old_p
            total += p * x
            old_p = new_p
        return total

    def Render(self):
        """Generates a sequence of points suitable for plotting.

        An empirical CDF is a step function; linear interpolation
        can be misleading.

        Returns:
            tuple of (xs, ps)
        """
        
        xs = [self.xs[0]]
        ps = [0.0]
        curProb = 0.0
        for i, p in enumerate(self.ps):
            xs.append(self.xs[i])
            curProb += p
            ps.append(curProb)

            try:
                xs.append(self.xs[i+1])
                ps.append(curProb)
            except IndexError:
                pass
        return xs, ps

def MakeOrganismPmfFromOrganisms(organisms):
    
    pmf = OrganismPmf()
    
    for organism in organisms:
        pmf.AddOrganism(organism)
    
    pmf.Normalize()
    
    return pmf

def MakeCdfFromOrganismPmf(orgPmf):
    
    xs, ys = orgPmf.Render()
    
    total = float(sum(ys))
    ys = tuple(y/total for y in ys)
    
    return Cdf(xs,ys)

# customize some matplotlib attributes
#matplotlib.rc('figure', figsize=(4, 3))

matplotlib.rc('font', size=14.0)
#matplotlib.rc('axes', labelsize=22.0, titlesize=22.0)
#matplotlib.rc('legend', fontsize=20.0)

#matplotlib.rc('xtick.major', size=6.0)
#matplotlib.rc('xtick.minor', size=3.0)

#matplotlib.rc('ytick.major', size=6.0)
#matplotlib.rc('ytick.minor', size=3.0)

def underride(d, **options):
    """Add key-value pairs to d only if key is not in d.

    If d is None, create a new dictionary.
    """
    if d is None:
        d = {}

    for key, val in options.iteritems():
        d.setdefault(key, val)

    return d

def plot(xs, ys, clf=True, root=None, line_options=None, **options):
    """plots a OrganismPmf or OrganismHist as a line.

    Args:
      OrganismPmf: OrganismHist or OrganismPmf object
      clf: boolean, whether to clear the figure      
      root: string filename root
      line_options: dictionary of options passed to pylot.plot
      options: dictionary of options
    """
    if clf:
        pyplot.clf()

    line_options = underride(line_options, linewidth=2)

    pyplot.plot(xs, ys, **line_options)
    save(root=root, **options)

def plotOrganismPmf(OrganismPmf, clf=True, root=None, line_options=None, **options):
    """plots a OrganismPmf or OrganismHist as a line.

    Args:
      OrganismPmf: OrganismHist or OrganismPmf object
      clf: boolean, whether to clear the figure      
      root: string filename root
      line_options: dictionary of options passed to pylot.plot
      options: dictionary of options
    """
    xs, ps = OrganismPmf.Render()
    line_options = underride(line_options, label=OrganismPmf.name)

    plot(xs, ps, clf, root, line_options, **options)

def plotOrganismHist(OrganismHist, clf=True, root=None, bar_options=None, **options):
    """plots a OrganismPmf or OrganismHist with a bar plot.

    Args:
      OrganismHist: OrganismHist or OrganismPmf object
      clf: boolean, whether to clear the figure
      root: string filename root
      bar_options: dictionary of options passed to pylot.bar
      options: dictionary of options
    """
    if clf:
        pyplot.clf()

    # find the minimum distance between adjacent values
    xs, fs = OrganismHist.Render()
    width = min(diff(xs))

    bar_options = underride(bar_options, 
                            label=OrganismHist.name,
                            align='center',
                            edgecolor='blue',
                            width=width)

    pyplot.bar(xs, fs, **bar_options)
    save(root=root, **options)

def plotCdf(cdf, clf=True, root=None, plot_options=dict(linewidth=2), 
    complement=False,transform=None,**options):
    """Plots a CDF as a line.

    Args:
      cdf: CDF objects
      clf: boolean, whether to clear the figure
      root: string root of the filename to write
      plot_options: sequence of option dictionaries
      complement: boolean, whether to plot the complementary CDF
      options: dictionary of keyword options passed along to Save
    """
    if clf:
        pyplot.clf()

    styles = options.get('styles', None)
    if styles is None:
        styles = '-'

    xs, ps = cdf.Render()

    if transform == 'exponential':
        complement = True
        options['yscale'] = 'log'

    if transform == 'pareto':
        complement = True
        options['yscale'] = 'log'
        options['xscale'] = 'log'

    if complement:
        ps = [1.0-p for p in ps]

    if transform == 'weibull':
        xs.pop()
        ps.pop()
        ps = [-math.log(1.0-p) for p in ps]
        options['xscale'] = 'log'
        options['yscale'] = 'log'

    if transform == 'gumbel':
        xs.pop(0)
        ps.pop(0)
        ps = [-math.log(p) for p in ps]
        options['yscale'] = 'log'

    line = pyplot.plot(xs, ps,
                       styles,
                       label=cdf.name,
                       **plot_options
                       )

    save(root, **options)

def diff(t):
    """Compute the differences between adjacent elements in a sequence.

    Args:
        t: sequence of number

    Returns:
        sequence of differences (length one less than t)
    """
    diffs = [t[i+1] - t[i] for i in range(len(t)-1)]
    return diffs

def save(root=None, formats=None, **options):
    """Generate plots in the given formats.

    Pulls options out of the option dictionary and passes them to
    title, xlabel, ylabel, xscale, yscale, axis and legend.

    Args:
      root: string filename root
      formats: list of string formats
      options: dictionary of options
    """
    title = options.get('title', '')
    pyplot.title(title)

    xlabel = options.get('xlabel', '')
    pyplot.xlabel(xlabel)

    ylabel = options.get('ylabel', '')
    pyplot.ylabel(ylabel)

    if 'xscale' in options:
        pyplot.xscale(options['xscale'])

    if 'yscale' in options:
        pyplot.yscale(options['yscale'])

    if 'axis' in options:
        pyplot.axis(options['axis'])

    loc = options.get('loc', 0)
    legend = options.get('legend', True)
    if legend:
        pyplot.legend(loc=loc)

    if formats is None:
        formats = ['eps', 'png', 'pdf']

    if root:
        for format in formats:
            saveFormat(root, format)

    show = options.get('show', False)
    if show:
        pyplot.show()
        
def saveFormat(root, format='eps'):
    """Writes the current figure to a file in the given format.

    Args:
      root: string filename root

      format: string format
    """
    filename = '%s.%s' % (root, format)
    print 'Writing', filename
    pyplot.savefig(filename, format=format, dpi=300)

def drawOrganismPmfAsCdf(orgPmf, generationNumber, bestFitness):
    pyplot.clf()
    plotCdf(MakeCdfFromOrganismPmf(orgPmf))
    pyplot.xlabel('Fitness')
    pyplot.ylabel('Probability')
    pyplot.title('Generation #%d: CDF of Fitnesses. Best: %.2f'%(generationNumber, bestFitness))
    pyplot.draw()

if __name__ == '__main__':
    import BooleanLogic#, testOrgs
    testOrganism = BooleanLogic.BooleanLogicOrganism('TestCode/andTest.v',2,1,randomInit=True,moduleName='andTest')
    #print testOrganism
    
    #defaultResult = testOrgs.testOrganism('TestCode/andTest.v', '.', 2, 1, 'andTest',clearFiles=True)
    #simMap = testOrgs.SimulationMap(defaultResult)
    
    #testOrganism.evaluate(simMap)
    
    #from copy import deepcopy
    
    fakeTestOrganisms = [testOrganism]
    for i in xrange(5):
        tst = deepcopy(testOrganism)
        fakeTestOrganisms.append(tst)
        
    for org in fakeTestOrganisms:
        org.fitness = random.randint(0,2)

    print ['%.2f'%organism.getFitness() for organism in fakeTestOrganisms]
    fakeTestOrganisms.sort()
    print ['%.2f'%organism.getFitness() for organism in fakeTestOrganisms]
    
    a = MakeOrganismPmfFromOrganisms(fakeTestOrganisms)
    drawOrganismPmfAsCdf(a,0)
    
    c = 0.0
    for i in xrange(1000):
        if a.Random() == testOrganism:
            c+=1.0
    print 'Probability of drawing a specific organism:\n\tActual: %.3f.\n\tSim: %.3f'%(a.Prob(testOrganism),c/1000)
    pyplot.show()
