#!/usr/bin/env python
from __future__ import print_function
from collections import OrderedDict
import re

regexes = {
    'NGI-RNAseq': ['v_ngi_rnaseq.txt', r"(\S+)"],
    'Nextflow': ['v_nextflow.txt', r"(\S+)"],
    'FastQC': ['v_fastqc.txt', r"FastQC v(\S+)"],
    'Cutadapt': ['v_cutadapt.txt', r"(\S+)"],
    'Trim Galore!': ['v_trim_galore.txt', r"version (\S+)"],
    'STAR': ['v_star.txt', r"(\S+)"],
    'HISAT2': ['v_hisat2.txt', r"version (\S+)"],
    'StringTie': ['v_stringtie.txt', r"(\S+)"],
    'Preseq': ['v_preseq.txt', r"Version: (\S+)"],
    'featureCounts': ['v_featurecounts.txt', r"featureCounts (\S+)"],
    'Picard MarkDuplicates': ['v_markduplicates.txt', r"([\d\.]+)"],
    'Samtools': ['v_samtools.txt', r"samtools (\S+)"],
    'MultiQC': ['v_multiqc.txt', r"multiqc, version (\S+)"],
}
results = OrderedDict()
results['NGI-RNAseq'] = '<span style="color:#999999;\">N/A</span>'
results['Nextflow'] = '<span style="color:#999999;\">N/A</span>'
results['FastQC'] = '<span style="color:#999999;\">N/A</span>'
results['Cutadapt'] = '<span style="color:#999999;\">N/A</span>'
results['Trim Galore!'] = '<span style="color:#999999;\">N/A</span>'
results['STAR'] = False
results['HISAT2'] = False
results['StringTie'] = '<span style="color:#999999;\">N/A</span>'
results['Preseq'] = '<span style="color:#999999;\">N/A</span>'
results['featureCounts'] = '<span style="color:#999999;\">N/A</span>'
results['Picard MarkDuplicates'] = '<span style="color:#999999;\">N/A</span>'
results['Samtools'] = '<span style="color:#999999;\">N/A</span>'
results['MultiQC'] = '<span style="color:#999999;\">N/A</span>'

# Search each file using its regex
for k, v in regexes.items():
    with open(v[0]) as x:
        versions = x.read()
        match = re.search(v[1], versions)
        if match:
            results[k] = "v{}".format(match.group(1))

# Strip STAR or HiSAT2
for k in results:
    if not results[k]:
        del(results[k])

# Dump to YAML
print ('''
id: 'software_versions'
section_name: 'NGI-RNAseq Software Versions'
section_href: 'https://github.com/SciLifeLab/NGI-RNAseq'
plot_type: 'html'
description: 'are collected at run time from the software output.'
data: |
    <dl class="dl-horizontal">
''')
for k,v in results.items():
    print("        <dt>{}</dt><dd>{}</dd>".format(k,v))
print ("    </dl>")
