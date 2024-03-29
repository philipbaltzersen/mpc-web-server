CREATE TABLE analyses (
    id UUID PRIMARY KEY,
    owners TEXT[] NOT NULL,
    file_names TEXT[] NOT NULL,
    statistical_method TEXT NOT NULL,
    method_arguments JSONB
);

CREATE TABLE results (
    id UUID PRIMARY KEY,
    analysis_id UUID NOT NULL REFERENCES analyses(id) ON DELETE CASCADE,
    result JSONB NOT NULL
);

CREATE TABLE data (
    entry_id SERIAL PRIMARY KEY,
    owner TEXT NOT NULL,
    data JSONB NOT NULL
);

INSERT INTO data (owner, data) 
VALUES ('do1', '{"before": 107.64052345967664, "after": 99.94079073157606}'),
       ('do1', '{"before": 94.00157208367223, "after": 82.94841736234198}'),
       ('do1', '{"before": 99.78737984105739, "after": 88.13067701650901}'),
       ('do1', '{"before": 112.40893199201457, "after": 76.45904260698275}'),
       ('do1', '{"before": 108.67557990149967, "after": 59.470101841659215}'),
       ('do1', '{"before": 80.22722120123589, "after": 91.5361859544036}'),
       ('do1', '{"before": 99.50088417525589, "after": 93.64436198859505}'),
       ('do1', '{"before": 88.48642791702302, "after": 77.57834979593558}'),
       ('do2', '{"before": 88.96781148206442, "after": 107.69754623987608}'),
       ('do2', '{"before": 94.10598501938372, "after": 70.45634325401235}'),
       ('do2', '{"before": 91.44043571160879, "after": 85.45758517301446}'),
       ('do2', '{"before": 104.54273506962976, "after": 83.12816149974167}'),
       ('do2', '{"before": 97.61037725146994, "after": 100.32779214358457}'),
       ('do2', '{"before": 91.21675016492829, "after": 99.69358769900285}'),
       ('do2', '{"before": 94.43863232745426, "after": 86.54947425696916}'),
       ('do2', '{"before": 93.33674327374267, "after": 88.78162519602174}');
