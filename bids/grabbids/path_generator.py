from collections import OrderedDict

def make_inside_path(subject=None, session=None, run=None, 
              data_type=None, acquisition=None, 
              task=None, root_folder=None, 
              modality=None, extension=None,
              reconstruction=None):
    
    root_folder = '' if root_folder is None else root_folder
    data_type = '' if data_type is None else data_type
    scope = locals()
    overall_template = ''
    
    keys = ('subject', 'session',  'task',
            'acquisition', 'reconstruction' ,'run', 
            'modality_suffix', 'extension')
    values = (subject, session, task,  
              acquisition, reconstruction ,
              run, modality, extension)
    
    val_dict = OrderedDict(zip(keys, values))
    
    patterns = ('sub-{}', '_ses-{}', '_task-{}', '_acq-{}', '_rec-{}','_run-{}', '_{}', '.{}')
    
    flags=[True if val_dict[item] is not None else False for item in keys]
    
    replacements = [patterns[i].format(values[i]) if flags[i] else '' for i in range(len(keys))]
    template_dict = OrderedDict(zip(keys, replacements))
    
    filename = ''.join(replacements)
    
    folder = '/{}/{}/{}/{}/'.format(root_folder, template_dict['subject'],
                               template_dict['session'][1:], data_type )
    folder = folder.split('/')
    #print(folder)
    folder = [item for item in folder if item != '']
    folder = '/' + '/'.join(folder) + '/'
    
    return folder + filename
