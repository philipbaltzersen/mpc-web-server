CREATE TABLE analyses (
    id UUID PRIMARY KEY,
    owners TEXT[] NOT NULL,
    data_files JSONB NOT NULL,
    statistical_method TEXT NOT NULL,
    method_arguments JSONB
);

CREATE TABLE results (
    id UUID PRIMARY KEY,
    analysis_id UUID NOT NULL REFERENCES analyses(id) ON DELETE CASCADE,
    result JSONB NOT NULL
);
